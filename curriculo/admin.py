from django.contrib import admin

from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'etiqueta', 'tipo']
    search_fields = ['nome', 'tipo']
    list_filter = ['tipo']

admin.site.register(Curso,CursoAdmin)
