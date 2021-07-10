from django.db.models import Count, Prefetch, Sum, F
from django.shortcuts import render
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import JsonResponse

from easy_pdf.views import PDFTemplateView

import json
import functools

from rest_framework import viewsets

from articles.models import Article

from orders.models import *
from orders.serializers import *
from io import StringIO
# Create your views here.

class OrdersViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	#filter_fields = ('urgent','order_type_id', {'deliver_date': ['exact', 'isnull']},'customer__tipo_cliente_id')
	filter_fields = {
		'urgent': ['exact'],
		'order_type_id': ['exact'],
		'deliver_date': ['exact', 'isnull'],
		'customer__tipo_cliente_id': ['exact']
	}

def make_order(request):
	articles = Article.objects.all()
	return render(request, 'orders/make_order.html', context = {
														"articles": articles
													}
				 )
def save_order(request):
	#print(request.POST.get('articles'))
	#print(request.POST.get('urgent'))
	#print(True)

	if request.method == 'POST':
		order_type_id = int(request.POST.get('order_type_id', -1))
		warehouse_id = int(request.POST.get('warehouse_id', -1))
		isUrgent = True if request.POST.get('urgent') == "true" else False
		order = None
		errors = None
		order = Order(order_type_id = order_type_id,
					  order_number = Order.objects.count() + 1, 
					  customer_id = 1, 
					  urgent = isUrgent)
		validate_model_instance(order)

		response = {
			'order_number': order.order_number,
			'urgent': order.urgent,
			'order_type': order.order_type.name
		}
		for article in json.loads(request.POST.get('articles')):
			#print(article['quantity'])
			model_instance = ArticlesOrder(order = order, article_id = article['article_id'], quantity = article['quantity'])
			validate_model_instance(model_instance)

		if order_type_id == 1:
			model_instance = DetailOrderDistributionCenter(order = order, warehouse_id = warehouse_id)
		elif order_type_id == 2:
			model_instance = DetailOrderBranchOffice(order = order, reference = request.POST.get('reference'), branch_office_code = request.POST.get('sucursal_code'))
		elif order_type_id == 3:
			model_instance = DetailOrderAssociatedCompany(order = order,reference = request.POST.get('reference'), partner_code = request.POST.get('partner_code'))
		
		isValid, errors = validate_model_instance(model_instance)
		if not isValid:
			return JsonResponse(errors, status = 400, safe = False)

		return JsonResponse(response)

def orders_report(request):
	#Ordenes urgentes de clientes platinum que no han sido surtidas
	"""orders = (Order.objects.filter(order_type_id = 1, 
											 urgent = True, 
											 customer__tipo_cliente_id = 4, 
											 deliver_date__isnull = True)
										.annotate(
											 num_articles = Count('articles_details'))
										.select_related(
											'customer', 
											'order_type', 
											'customer__tipo_cliente')
										)"""
	return render(request, 'orders/report.html')

def validate_model_instance(instance):
	isValid = True
	json_resp = []
	try:
		instance.full_clean()
		instance.save()
	except ValidationError as e:
		io = StringIO(str(e).replace("'", '"'))
		json_resp = json.load(io)
		isValid = False

	return (isValid, json_resp)

def dashboard(request):
	orders = Order.objects.all().prefetch_related(
									Prefetch('articles_details', 
											queryset = (ArticlesOrder.objects.all()
														.select_related('article')))
														)
	total_orders = Order.objects.count()
	delivered_orders = Order.objects.exclude(deliver_date = None).count()
	pendding_orders = total_orders - delivered_orders
	delivery_percentaje = (delivered_orders / total_orders) * 100;
	amount = 0
	for order in orders:
		for detail in order.articles_details.all():
			amount += detail.article.price * detail.quantity


	return JsonResponse({'total_amount': amount, 
						 'orders_count': total_orders, 
						 'delivered_orders_count': delivered_orders,
						 'pendding_orders_count': pendding_orders,
						 'delivery_percentaje': delivery_percentaje
						 })

class OrderPDF(PDFTemplateView):
	template_name = "orders/pdfs/order_pdf.html"

	def get_context_data(self, order_id, order_type_id, **kwargs):


		select_related_relations = []
		if order_type_id == 1:
			select_related_relations.append('distribution_center_details')
			print('entra')
		elif order_type_id == 2:
			select_related_relations.append('branch_office_details')
			print('entra')
		elif order_type_id == 3:
			select_related_relations.append('associated_company_details')
			print('entra')



		orders = (Order.objects.
					select_related('customer', 
								   'order_type', 
								   'customer__tipo_cliente',
								   *select_related_relations)
					.prefetch_related(
						Prefetch('articles_details', 
							queryset = ArticlesOrder.objects
								.annotate(subtotal = Sum(F('quantity') * F('article__price')))
								.all().select_related('article') ) )
					.filter(pk = order_id)
				 )
		
		total = (orders.aggregate(total = Sum(F('articles_details__quantity') 
											* F('articles_details__article__price'))
								 )['total']

				)

		#Se usa el filter en vez del get para poder hacer la operación de total 
		#Todo: Almacenar los subtotales en la base de datos en la table de articles_details y el total en la de orden
		order = orders[0]
		context = {
			'order': order,
			'total': total
		}

		return super(OrderPDF, self).get_context_data(**context)