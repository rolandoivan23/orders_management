from django.shortcuts import render
from rest_framework import viewsets

from catalogs.models import *
from .serializers import *
# Create your views here.
class OrderTypeViewSet(viewsets.ModelViewSet):
	queryset = OrderType.objects.all()
	serializer_class = OrderTypeSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
	queryset = Warehouse.objects.all()
	serializer_class = WarehouseSerializer

class CustomerTypeViewSet(viewsets.ModelViewSet):
	queryset = CustomerType.objects.all()
	serializer_class = CustomerTypeSerializer