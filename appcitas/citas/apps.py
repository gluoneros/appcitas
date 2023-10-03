"""citas aplication module"""
from django.apps import AppConfig


class CitasConfig(AppConfig):
    """citas application cettings"""
    default_auto_field = "django.db.models.BigAutoField"
    
    name = "citas"
    verbose_name = 'citas'
