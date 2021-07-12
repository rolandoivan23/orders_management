from rest_framework import serializers
from vendors.models import *

class VendorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendor
		exclude = []