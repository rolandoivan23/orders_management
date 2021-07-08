
from django.conf.urls import url, include

app_name = 'catalogs'
urlpatterns = [
    url(r'^', include('catalogs.api.urls')),
]