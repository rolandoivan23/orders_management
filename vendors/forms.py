from django.forms import ModelForm

from .models import Vendor 
class VendorForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(self.fields)

	class Meta:
		model = Vendor
		exclude = []