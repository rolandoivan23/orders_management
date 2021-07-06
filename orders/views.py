from django.db.models import Count, Prefetch
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

import json
import functools

from rest_framework import viewsets

from articles.models import Article

from orders.models import *
from orders.serializers import *
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
		order = Order(order_type_id = order_type_id, order_number = Order.objects.count() + 1, customer_id = 1, urgent = isUrgent)
		order.save()
		for article in json.loads(request.POST.get('articles')):
			#print(article['quantity'])
			ArticlesOrder.objects.create(order = order, article_id = article['article_id'], quantity = article['quantity'])

		if order_type_id == 1:
			DetailOrderDistributionCenter.objects.create(order = order, warehouse_id = warehouse_id)
		elif order_type_id == 2:
			DetailOrderBranchOffice.objects.create(order = order, reference = request.POST.get('reference'), branch_office_code = request.POST.get('sucursal_code'))
		elif order_type_id == 3:
			DetailOrderAssociatedCompany.objects.create(order = order,reference = request.POST.get('reference'), partner_code = request.POST.get('partner_code'))

		return render(request, 'orders/make_order.html')

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
