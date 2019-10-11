from django.contrib import admin

# Register your models here.
from .models import Provincia, Ciudad

admin.site.register(Provincia)
admin.site.register(Ciudad)