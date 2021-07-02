from django.db import models

# Create your models here.
class Vendor(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 80)
	address = models.CharField(max_length = 120)
