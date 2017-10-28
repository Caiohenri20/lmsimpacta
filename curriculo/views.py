from django.views.generic import ListView

from django.shortcuts import render
from .models import Curso

class CursosListView(ListView):
     model = Curso