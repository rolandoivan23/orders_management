
from django.conf.urls import url, include

from articles.api.views import *

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    url(r'api/v1/', include(router.urls)),
]
