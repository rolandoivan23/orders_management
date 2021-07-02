from django.db import models

from articles.models import Article
from catalogs.models import Warehouse, OrderType
from customers.models import Customer

# Create your models here.
class Order(models.Model):
	id = models.AutoField(primary_key = True)
	order_number = models.IntegerField(unique = True)
	customer = models.ForeignKey(Customer, related_name = 'orders', on_delete = models.PROTECT)
	created_date = models.DateField(auto_now_add = True)
	deliver_date = models.DateField(null = True)
	urgent = models.BooleanField(default = False)
	order_type = models.ForeignKey(OrderType, related_name = 'orders', on_delete = models.PROTECT)

class DetailOrderDistributionCenter(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.ForeignKey(Order, related_name = 'distribution_center_orders', on_delete = models.PROTECT)
	warehouse = models.ForeignKey(Warehouse, related_name = 'orders', on_delete = models.PROTECT)

class DetailOrderBranchOffice(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.ForeignKey(Order, related_name = 'branch_office_orders', on_delete = models.PROTECT)
	reference = models.CharField(max_length = 20)
	branch_office_code = models.IntegerField()

class DetailOrderAssociatedCompany(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.ForeignKey(Order, related_name = 'associated_company_orders', on_delete = models.PROTECT)
	reference = models.CharField(max_length = 20)
	partner_code = models.IntegerField()

class ArticlesOrder(models.Model):
	id = models.AutoField(primary_key = True)
	article = models.ForeignKey(Article, related_name = 'orders', on_delete = models.PROTECT)
	order = models.ForeignKey(Order, related_name = 'articles_details', on_delete = models.PROTECT)
	quantity = models.IntegerField()