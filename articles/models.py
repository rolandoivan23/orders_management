from django.db import models

from vendors.models import Vendor

from django.urls import reverse

# Create your models here.
class Article(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField(max_length = 10)
	description = models.TextField(null = True)
	vendors = models.ManyToManyField(Vendor, related_name = 'articles', null = True)
	price = models.DecimalField(decimal_places = 4, max_digits = 12)

	def __str__(self):
		return "%s  -  %s" % (self.code, self.description)

	def get_absolute_url(self):
	        return reverse('article-show', kwargs={'pk': self.pk})