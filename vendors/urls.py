
from django.urls import path
from django.conf.urls import url, include
from vendors.views import *

app_name = 'vendors'
urlpatterns = [
    path('vendors', VendorListView.as_view(), name='vendors-list'),
    path('vendors/new/', VendorCreateView.as_view(), name='vendor-new'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor-show'),
    url(r'^', include('vendors.api.urls')),
]
