from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .choices import ALUNO, PROFESSOR
from .models import Usuario, Aluno, Professor, Coordenador
from .forms import (AlunoAlterarForm,AlunoForm,ProfessorAlterarForm,ProfessorForm,CoordenadorForm,CoordenadorAlterarForm)

class AlunoAdmin(UserAdmin):
    add_form = AlunoForm
    form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "curso")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "curso")}),)
    list_display = ["ra","nome","email","curso"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["curso"]

class ProfessorAdmin(UserAdmin):
    add_form = ProfessorForm
    form = ProfessorAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "apelido")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "apelido")}),)
    list_display = ["ra","nome","email","apelido"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = []

class CoordenadorAdmin(UserAdmin):
    add_form = CoordenadorForm
    form = CoordenadorAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "sala")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "sala")}),)
    list_display = ["ra","nome","email","sala"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = []

admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Coordenador,CoordenadorAdmin)
admin.site.unregister(Group)
