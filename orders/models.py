from django.db import models

# Create your models here.
class MailOrder(models.Model):
  nombre = models.TextField(null=False)
  email = models.EmailField(null=False)
  phone = models.TextField(null=True)
  fecha = models.DateTimeField(auto_now_add=True)
  mensaje = models.TextField(null=False)

  def __str__(self):
    return f"{self.nombre} {self.email} {self.fecha}"

"""
class Pedido(models.Model):
    nombres = models.TextField()
    apellidos = models.TextField()
    direccion = models.CharField(max_length=1)
    correo = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='pedidos')
    cantidad = models.IntegerField()
 """
