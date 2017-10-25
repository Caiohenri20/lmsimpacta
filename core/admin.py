from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    ordering = ["ra"]
    list_display = ["ra","primeiro_nome","ultimo_nome","email"]
    list_filter = ["perfil"]
    filter_horizontal = []

admin.site.register(Usuario, UsuarioAdmin)
