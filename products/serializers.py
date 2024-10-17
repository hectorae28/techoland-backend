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
"""
class CategoriasSerializer(serializers.ModelSerializer):
  CategoriaGrosor = GrosorSerializer(many=True)
  class Meta:
    model = Categoria
    fields = ['id','nombre','CategoriaGrosor']
"""
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
  #ProductoCategoria = CategoriasSerializer(many=True)
  ProductoImagen = ImageSerializer(many=True)
  class Meta:
    model = Producto
    fields = ['id','nombre','slug','info' , 'descripcion','ProductoImagen']

class ProductosListSerializer(serializers.ModelSerializer):
  ProductoImagen = ImageSerializer(many=True)
  class Meta:
    model = Producto
    fields = ['id', 'nombre','slug', 'descripcion' ,'ProductoImagen']
"""
class CategoriasListSerializer(serializers.ModelSerializer):
    product = ProductosListSerializer()
    CategoriaGrosor = GrosorSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ['id','nombre','CategoriaGrosor','product']
"""

