
from django.conf.urls import url, include

from catalogs.api.views import *

from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    url(r'api/v1/', include(router.urls)),
]
