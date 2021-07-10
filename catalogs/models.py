from django.db import models

# Create your models here.
class CustomerType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 60)
	description = models.TextField()
	key = models.CharField(max_length = 50, unique = True)

class OrderType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 60)
	description = models.TextField(null = True)
	key = models.CharField(max_length = 50, unique = True)

	def __str__(self):
		return self.name

	def abc_validator(self, xp):
		print(xp)
		return True

class Warehouse(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField(max_length = 60)
	address = models.CharField(max_length = 120)