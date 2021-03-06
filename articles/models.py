from django.db import models

from vendors.models import Vendor

from django.urls import reverse

from django.core.validators import *

# Create your models here.
class Article(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField(max_length = 10)
	description = models.TextField(null = True)
	vendors = models.ManyToManyField(Vendor)
	price = models.DecimalField(decimal_places = 4, max_digits = 12, validators=[MinValueValidator(0)])

	def __str__(self):
		return "%s  -  %s" % (self.code, self.description)

	def get_absolute_url(self):
	        return reverse('articles:article-show', kwargs={'pk': self.pk})