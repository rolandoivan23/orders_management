from rest_framework import serializers
from catalogs.models import *

class OrderTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderType
		exclude = []

class WarehouseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Warehouse
		exclude = []