from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.TextField( max_length=200 )
    slug = models.SlugField( max_length=200, unique=False )
    descripcion = models.TextField( max_length=500 )
    info = models.JSONField(default=dict)
    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ProductoImagen')
    product_image = models.ImageField(upload_to='images/',null=True)
    image_src = models.TextField(default='/')
    def __str__(self):
        return f"{self.product.nombre} {self.id}"

class Grosor(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ProductoGrosor')
    grosor = models.TextField(max_length=100, default='default')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.product.nombre} {self.grosor} {self.precio}"

class Color(models.Model):
    grosor = models.ForeignKey(Grosor, on_delete=models.CASCADE, related_name='GrosorColores')
    color = models.TextField(default='default')
    def __str__(self):
        return f"{self.grosor} de Color {self.color}" #self.color


