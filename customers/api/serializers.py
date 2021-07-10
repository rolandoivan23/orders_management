from rest_framework import serializers
from customers.models import *

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		exclude = []