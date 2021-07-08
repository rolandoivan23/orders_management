
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import VendorForm
from .models import *

class VendorListView(ListView):
    model = Vendor

class VendorDetailView(DetailView):
    model = Vendor

class VendorCreateView(CreateView):
	model = Vendor
	#fields = ['code', 'description', 'price']
	form_class = VendorForm

class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name_suffix = '_update_form'

class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendors:vendors-list')