from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from .models import MailOrder


class MailOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = MailOrder
    fields = '__all__'
  def create(self, validated_data):
    send_mail(
      subject="Mensaje de la web",
      message=f""" mensaje de la paguina web:
        nombre: {validated_data['nombre']},
        email: {validated_data['email']},
        telefono: {validated_data['phone']},
        mensaje: "{validated_data['mensaje']}"
      """,
      from_email="harcher5c@gmail.com",
      recipient_list=['hectorae28@gmail.com'],
    )
    return MailOrder.objects.create(**validated_data)