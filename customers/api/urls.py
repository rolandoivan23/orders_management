
from django.conf.urls import url, include

from customers.api.views import *

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    url(r'api/v1/', include(router.urls)),
]
