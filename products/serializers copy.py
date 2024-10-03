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
class CategoriasSerializer(serializers.ModelSerializer):
  grosor = GrosorSerializer(many=True)
  class Meta:
    model = Categoria
    fields = ['id','nombre','grosor']
    
class ProductoSerializer(serializers.ModelSerializer):
  categoria = CategoriasSerializer()
  class Meta:
    model = Producto
    fields = ['id','nombre','slug','descripcion','product_image','categoria']
class ProductosListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = '__all__'



