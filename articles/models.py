from django.db import models

from vendors.models import Vendor

# Create your models here.
class Article(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField(max_length = 10)
	description = models.TextField(null = True)
	vendors = models.ManyToManyField(Vendor, related_name = 'articles')
