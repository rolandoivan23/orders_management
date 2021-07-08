from rest_framework import serializers
from articles.models import *

class ArticleSerializer(serializers.ModelSerializer):
	vendors = serializers.StringRelatedField(many = True)
	class Meta:
		model = Article
		exclude = []