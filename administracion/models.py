from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Convocatoria(models.Model):
    activa = models.BooleanField()


class Contacto(models.Model):
    datos = models.TextField()


class AcercaDe(models.Model):
    datos = models.TextField()


class Premios(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Mensaje(models.Model):
    remitente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default = False)

    def __str__(self):
        return self.asunto

