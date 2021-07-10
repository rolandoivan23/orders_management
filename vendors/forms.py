from django.forms import ModelForm

from .models import Vendor 
class VendorForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['articles'].required = False

	class Meta:
		model = Vendor
		exclude = []