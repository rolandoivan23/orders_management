from django.test import TestCase
from catalogs.models import *

# Create your tests here.
class CatalogsTest(TestCase):

	def test_customer_types_catalog(self):
		customer_types = (CustomerType.objects.values_list('name', 'key', 'id')
										.order_by('pk'))

		types_list = [
			{
		        "id": 1,
		        "name": "Normal",
		        "key": "normal"
		    },
		    {
		        "id": 2,
		        "name": "Plata",
		        "key": "plata"
		    },
		    {
		        "id": 3,
		        "name": "Oro",
		        "key": "oro"
		    },
		    {
		        "id": 4,
		        "name": "Platinum",
		        "key": "platinum"
		    }
		]
		#Type 0 means the first key in the object(element of list types_list)
		sorted_types = sorted(types_list, key = lambda type: type['id'] )
		for i, tuple_type in enumerate(customer_types):
			self.assertEqual(tuple_type , (sorted_types[i]['name'], 
										   sorted_types[i]['key'],
										   sorted_types[i]['id'] )
							)

	def test_order_types_catalog(self):
		order_types = (OrderType.objects.values_list('name', 'key', 'id')
										.order_by('pk'))

		types_list = [
			{
		        "id": 1,
		        "name": "Al centro de distribución",
		        "key": "al_centro_de_distribucion"
		    },
		    {
		        "id": 2,
		        "name": "Orden a sucursal",
		        "key": "orden_a_sucursal"
		    },
		    {
		        "id": 3,
		        "name": "Orden a empresa asociada",
		        "key": "orden_a_empresa_asociada"
		    }
		]
		sorted_types = sorted(types_list, key = lambda type: type['id'] )
		for i, type_tuple in enumerate(order_types):
			self.assertEqual( type_tuple, (sorted_types[i]['name'], 
										   sorted_types[i]['key'],
										   sorted_types[i]['id'] )
							)

	def test_patter_key_match(self):
		order_type = OrderType.objects.last()
		self.assertEqual(check_key_pattern(order_type.key, 
										   order_type.name),
										   True) 