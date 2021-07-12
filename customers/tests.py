from django.test import TestCase

from customers.models import *
# Create your tests here.
class CustomersTests(TestCase):

	def test_customer_1_exists(self):
		customer_exists = Customer.objects.filter(pk = 1).exists()
		self.assertTrue(customer_exists)