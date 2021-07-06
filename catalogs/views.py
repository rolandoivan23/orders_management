from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.
class OrderTypeViewSet(viewsets.ModelViewSet):
	queryset = OrderType.objects.all()
	serializer_class = OrderTypeSerializer