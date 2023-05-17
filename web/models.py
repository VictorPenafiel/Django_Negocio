import uuid
from django.db import models


# Create your models here.


class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    price = models.IntegerField()
    slug = models.SlugField()
    is_private = models.BooleanField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Sucursales(models.Model):
    sucursales_uuid = models.UUIDField()
    direccion = models.CharField(max_length=64)
    telefono = models.IntegerField()
    image_url = models.URLField()
    horario= models.CharField(max_length=64)
    correo = models.CharField(max_length=64)
    is_private = models.BooleanField()
