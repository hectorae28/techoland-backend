from rest_framework import serializers
from .models import *

class ColorSerializer(serializers.ModelSerializer):
  #grosor = GrosorSerializer()
  class Meta:
    model = Color
    fields = ['id','color']

class GrosorSerializer(serializers.ModelSerializer):
  GrosorColores = ColorSerializer(many=True)
  class Meta:
    model = Grosor
    fields = [ 'id','grosor','precio', 'GrosorColores']

class ImagenProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ImagenProducto
    fields = ['product_image']

class ProductoSerializer(serializers.ModelSerializer):
  ProductoGrosor = GrosorSerializer(many=True)
  ProductoImagen = ImagenProductoSerializer(many=True)
  class Meta:
    model = Producto
    fields = ['id','nombre','slug','descripcion','info','ProductoGrosor', 'ProductoImagen']
    lookup_field = 'slug'

class ProductosListSerializer(serializers.ModelSerializer):
  ProductoImagen = ImagenProductoSerializer(many=True)
  class Meta:
    model = Producto
    fields = fields = ['id','nombre','slug','descripcion', 'ProductoImagen']

""" class CategoriasListSerializer(serializers.ModelSerializer):
    product = ProductosListSerializer()
    CategoriaGrosor = GrosorSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ['product','id','nombre','info','CategoriaGrosor',] """


