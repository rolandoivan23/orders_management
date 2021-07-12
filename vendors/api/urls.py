
from django.conf.urls import url, include

from vendors.api.views import *

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'vendors', VendorsViewSet)

urlpatterns = [
    url(r'api/v1/', include(router.urls)),
]