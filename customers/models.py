from django.db import models

from catalogs.models import CustomerType 

# Create your models here.
class Customer(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 80)
	code = models.CharField(max_length = 10)
	address = models.CharField(max_length = 120)
	tipo_cliente = models.ForeignKey(CustomerType, related_name = 'customers', on_delete = models.PROTECT)