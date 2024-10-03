from rest_framework import viewsets
from .models import *
from .serializers import *

class MailOrderViewSet(viewsets.ModelViewSet):
  queryset = MailOrder.objects.all()
  serializer_class = MailOrderSerializer