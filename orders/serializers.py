from rest_framework import serializers
from orders.models import *

class OrderSerializer(serializers.ModelSerializer):
	customer = serializers.StringRelatedField()
	order_type = serializers.StringRelatedField()
	num_articles = serializers.IntegerField(
	    source='articles_details.count', 
	    read_only=True
	)
	class Meta:
		model = Order
		exclude = []