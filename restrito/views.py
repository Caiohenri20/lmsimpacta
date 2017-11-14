from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from curriculo.models import Turma, DisciplinaOfertada
from .checkers import check_aluno, check_professor

@login_required(login_url="/entrar")
@user_passes_test(check_aluno, login_url="/")
def aluno(request):
    contexto = {
        "turmas": Turma.objects.filter(alunos__parent_link=request.user)
    }
    return render(request,"restrito/aluno.html",contexto)

@login_required(login_url="/entrar")
@user_passes_test(check_aluno, login_url="/")
def matricula(request):
    contexto = {}
    if request.POST:
        ano = request.POST.get("ano",0)
        semestre = request.POST.get("semestre",0)
        turmas = Turma.objects.filter(disciplina_ofertada__ano=ano, disciplina_ofertada__semestre=semestre)
        for turma in turmas:
            print(turma.alunos)
            
        contexto["turmas"] = turmas
    else:
        pass
    return render(request,"restrito/matricula.html",contexto)

@login_required(login_url="/entrar")
@user_passes_test(check_professor, login_url="/")
def professor(request):
    contexto = {

    }
    return render(request,"restrito/professor.html",contexto)