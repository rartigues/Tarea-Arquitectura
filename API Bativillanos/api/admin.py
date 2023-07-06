from django.contrib import admin
from .models import Villain, Power

# Register your models here.

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'universo',
    ]

@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = [
        'villano',
        'nombre',
    ]

