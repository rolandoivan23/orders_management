from django.db.models import Count
from django.shortcuts import render

from articles.models import Article

from orders.models import *

import json
# Create your views here.

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
	orders = Order.objects.filter(order_type_id = 1, urgent = True, customer__tipo_cliente_id = 4, deliver_date__isnull = True).annotate(num_articles = Count('articles_details')).select_related('customer', 'order_type')
	return render(request, 'orders/report.html', {'orders': orders})
