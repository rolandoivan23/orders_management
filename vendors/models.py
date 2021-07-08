from django.db import models
from django.urls import reverse


# Create your models here.
class Vendor(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 80)
	address = models.CharField(max_length = 120)
	articles = models.ManyToManyField('articles.Article', through='articles.article_vendors')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
	        return reverse('vendors:vendor-show', kwargs={'pk': self.pk})