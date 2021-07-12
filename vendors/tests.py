from django.test import TestCase
from vendors.models import *

# Create your tests here.
class VendorsTest(TestCase):

	def test_vendor_1_exists(self):
		vendors_exists = Vendor.objects.filter(pk = 1).exists()
		self.assertTrue(vendors_exists)