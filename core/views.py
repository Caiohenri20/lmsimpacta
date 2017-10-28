from django.shortcuts import render
from django.views.generic import TemplateView

from curriculo.models import Curso

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

def cursos(request):
    contexto = {
        "cursos_list" : Curso.objects.all()
    }
    return render(request,"lista_cursos.html",contexto)

def contato(request):
    if request.GET:
        return render(request,"contato.html")
    else:
        print(request.POST["nome"])
        print(request.POST["assunto"])
        print(request.POST["mensagem"])
        return render(request,"contato.html")

index = IndexView.as_view()