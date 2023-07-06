from django.db import models

class Villain(models.Model):
    nombre      = models.CharField(
        max_length=255, 
        blank=False,
    )

    universo    = models.CharField(
        max_length=255, 
        blank=False,
    )

    descripcion = models.TextField(
        blank=False
    )

    imagen      = models.TextField(
        null=False
    )

class  Power(models.Model):
    villano = models.ForeignKey(
        Villain, 
        on_delete=models.CASCADE,
        related_name='poderes',
        null=False,
    )

    nombre  = models.CharField(
        max_length=255, 
        blank=False,
    )

    def __str__(self):
        return self.nombre
