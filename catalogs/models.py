from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.
class CustomerType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 60)
	description = models.TextField()
	key = models.CharField(max_length = 50, unique = True)

	def clean(self):
		check_key_pattern(self.key, self.name)

class OrderType(models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 60)
	description = models.TextField(null = True)
	key = models.CharField(max_length = 50, unique = True)

	def __str__(self):
		return self.name
	
	def clean(self):
		check_key_pattern(self.key, self.name)


class Warehouse(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField(max_length = 60)
	address = models.CharField(max_length = 120)


"""
Recibe 2 cadenas como parámetro y verifica que estas sean iguales una vez que se 
transforma la cadena de nombre de un registro de un catálogo, ya transformado el 
nombre debe de ser igual que la llave(campo key) del registro introducido.
"""
def check_key_pattern(key, name, raise_exception = True):
	cleaned_name = name.replace(' ', '_').lower().strip()
	if not key.lower().strip() == cleaned_name:
		if raise_exception:
			raise ValidationError({"key": 'Key pattern not match respect name'})
		else:
			return False
	return True