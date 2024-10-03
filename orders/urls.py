from django.urls import path, include
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register('orders', MailOrderViewSet,"orders")

urlpatterns = [
  path('',include(router.urls)),
]