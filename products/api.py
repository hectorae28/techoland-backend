from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

class AccesoriosViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Producto.objects.filter(slug='accesorio')
  serializer_class = ProductoSerializer

class ProductosListViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Producto.objects.all().exclude(slug='accesorio')
  serializer_class = ProductosListSerializer
  
class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer
  lookup_field = 'slug'

class ColorViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Color.objects.all()
  serializer_class = ColorSerializer

class GrosorViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Grosor.objects.all()
  serializer_class = GrosorSerializer

""" class CategoriasListViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Categoria.objects.all().exclude(product__slug='accesorio')
  serializer_class = CategoriasListSerializer """
