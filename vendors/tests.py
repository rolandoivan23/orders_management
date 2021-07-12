from django.test import TestCase
from vendors.models import *

# Create your tests here.
class VendorsTest(TestCase):

	def test_articles_assigned_at_least_one_vendor(self):
		vendors_with_articles = Vendor.objects.exclude(articles = None).count()
		self.assertGreater(vendors_with_articles, 0)