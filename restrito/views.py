from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from curriculo.models import Turma

@login_required(login_url="/entrar")
def aluno(request):
    contexto = {
        "turmas": Turma.objects.filter(alunos__parent_link=request.user)
    }
    return render(request,"restrito/aluno.html",contexto)

@login_required(login_url="/entrar")
def professor(request):
    contexto = {

    }
    return render(request,"restrito/professor.html",contexto)