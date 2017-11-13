from django.views.generic import ListView
from django.shortcuts import render

from .models import Curso

class CursosListView(ListView):
    model = Curso

def curso(request, sigla):
    contexto = {
        "curso":Curso.objects.get(sigla=sigla)
    }
    return render(request,"curriculo/curso.html",contexto)