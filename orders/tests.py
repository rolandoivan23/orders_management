from django.test import TestCase, Client
from django.urls import reverse

import json

from orders.views import Order, validate_model_instance
from catalogs.models import OrderType, CustomerType
from customers.models import Customer

# Create your tests here.
class OrdersReport(TestCase):

	def test_validate_model_instance(self):
		try:
			order_type_id = OrderType.objects.values_list('id').last()[0]
			customer_id = Customer.objects.values_list('id').last()[0]
		except Exception:
			order_type_id = OrderType.objects.create(name = 'Tipo orden de prueba', 
							 description = 'Just for test',
							 key = 'tipo_orden_de_prueba').pk
			
			customer_type = None
			try:
				customer_type_id = CustomerType.objects.values_list('id').last()[0]
			except Exception:
				customer_type = CustomerType.objects.create(
						name = 'Tipo 1',
						description = 'Just for test',
						key = 'tipo_1'
					).pk

			try:
				customer_id = Customer.objects.values_list('id').first()[0]
			except Exception:
				customer_id = Customer.objects.create(name = 'Tipo orden de prueba', 
							 code = 'Just for test',
							 address = 'tipo_orden_de_prueba',
							 tipo_cliente_id = customer_type_id).pk

		order = Order(order_type_id = order_type_id,
					  order_number = Order.objects.count() + 1, 
					  customer_id = customer_id, 
					  urgent = False)

		self.assertTrue( validate_model_instance(order) )

	
	def test_make_test(self):
		data = {
			"articles": "[{\"article_id\":\"1\",\"quantity\":\"1\"}]", 
			"order_type_id": "1",
			"urgent": "true",
			"warehouse_id": "1"
		}
		response = Client().post(reverse('save_order'), data)  
		self.assertEqual(response.status_code, 200)
		excpected_response = {
			"order_type": 'Al centro de distribución',
			"urgent": True,
		}
		decoded_resp = json.loads(response.content.decode())
		del decoded_resp['order_number']
		self.assertEqual(decoded_resp, excpected_response)
		
		data = {
			"order_type_id": "1",
			"urgent": "true",
			"warehouse_id": "1"
		}
		response = Client().post(reverse('save_order'), data)  
		self.assertEqual(response.status_code, 400)