from django.contrib import admin

# Register your models here.
from .models import * # * importa toat

admin.site.register(Task)