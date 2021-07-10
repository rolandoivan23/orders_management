from django.db import models

from articles.models import Article
from catalogs.models import Warehouse, OrderType
from customers.models import Customer
from django.core.validators import *


"""
Regex paa patron donde los primeros 2 caracteres deben de ser una letra de la a a la z 
y los siguientes caracteres cualquier valor numérico valido
"""
REFERENCE_FIELD_REGEX = RegexValidator(r'[A-Za-z]{2}[0-9]$', 'Formato de referencia incorrecto')

# Create your models here.
class Order(models.Model):
	id = models.AutoField(primary_key = True)
	order_number = models.IntegerField(unique = True, validators=[MinValueValidator(1)])
	customer = models.ForeignKey(Customer, related_name = 'orders', on_delete = models.PROTECT)
	created_date = models.DateField(auto_now_add = True)
	deliver_date = models.DateField(null = True, blank = True)
	urgent = models.BooleanField(default = False)
	order_type = models.ForeignKey(OrderType, related_name = 'orders', on_delete = models.PROTECT)

class DetailOrderDistributionCenter(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.OneToOneField(Order, related_name = 'distribution_center_details', on_delete = models.PROTECT)
	warehouse = models.ForeignKey(Warehouse, related_name = 'orders', on_delete = models.PROTECT)

class DetailOrderBranchOffice(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.OneToOneField(Order, related_name = 'branch_office_details', on_delete = models.PROTECT)
	reference = models.CharField(max_length = 20, validators=[REFERENCE_FIELD_REGEX])
	branch_office_code = models.IntegerField(validators=[MinValueValidator(1)])

class DetailOrderAssociatedCompany(models.Model):
	id = models.AutoField(primary_key = True)
	order = models.OneToOneField(Order, related_name = 'associated_company_details', on_delete = models.PROTECT)
	reference = models.CharField(max_length = 20, validators=[REFERENCE_FIELD_REGEX])
	partner_code = models.IntegerField(validators=[MinValueValidator(1)])

class ArticlesOrder(models.Model):
	id = models.AutoField(primary_key = True)
	article = models.ForeignKey(Article, related_name = 'orders', on_delete = models.PROTECT)
	order = models.ForeignKey(Order, related_name = 'articles_details', on_delete = models.PROTECT)
	quantity = models.IntegerField(validators=[MinValueValidator(1)])