"""orders_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from orders.views import make_order, save_order, orders_report
from articles.views import ArticlesViewSet
from catalogs.views import *

from rest_framework.routers import SimpleRouter

from orders.views import OrdersViewSet

router = SimpleRouter()
router.register(r'orders', OrdersViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'order_types', OrderTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^make_order$', make_order, name = 'make_order'),
    url(r'^save_order$', save_order, name = 'save_order'),
    url(r'^orders_report$', orders_report, name = 'orders_report'),
    url(r'api/v1/', include(router.urls)),
]
