from django.contrib import admin

# IMPORTAMOS EL UserAdmin
from django.contrib.auth.admin import UserAdmin

# IMPORTAMOS EL MODELO
from .models import User

# Register your models here.
admin.site.register(User)
