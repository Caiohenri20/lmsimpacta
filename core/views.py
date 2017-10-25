from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

def contato(request):
    if request.GET:
        return render(request,"contato.html")
    else:
        print(request.POST["nome"])
        print(request.POST["assunto"])
        print(request.POST["mensagem"])
        return render(request,"contato.html")

index = IndexView.as_view()