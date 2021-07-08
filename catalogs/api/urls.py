
from django.conf.urls import url, include

from catalogs.api.views import *

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'order_types', OrderTypeViewSet)
router.register(r'warehouses', WarehouseViewSet)


urlpatterns = [
    url(r'api/v1/', include(router.urls)),
]
