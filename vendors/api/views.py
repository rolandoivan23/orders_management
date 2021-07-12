from .serializers import *
from rest_framework import viewsets

from vendors.models import Vendor
# Create your views here.
class VendorsViewSet(viewsets.ModelViewSet):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer