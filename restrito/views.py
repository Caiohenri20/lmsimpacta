from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse

from curriculo.models import Turma, DisciplinaOfertada

from .models import Questao
from .checkers import check_aluno, check_professor
from .forms import QuestaoForm

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
    turmas = Turma.objects.filter(professor__parent_link=request.user)
    for turma in turmas:
        turma.exercicios = Questao.objects.filter(turma=turma)
    contexto = {
        "turmas": turmas
    }
    return render(request,"restrito/professor.html",contexto)

@login_required(login_url="/entrar")
@user_passes_test(check_professor, login_url="/")
def questao_form(request, turma_id, questao_id=None):
    turma = Turma.objects.get(id=turma_id)
    if questao_id:
        qst = Questao.objects.get(id=questao_id)
        numero = qst.numero
    else:
        qst = Questao(turma=turma)
        numero = 'Nova'
    form = QuestaoForm(request.POST or None, request.FILES or None, instance=qst)
    if request.POST and form.is_valid():
        form.save()        
        return redirect(reverse('restrito:professor'))
    
    contexto = {
        "form":form,
        "turma": turma,
        'numero': numero
    }
    return render(request, "restrito/questao.html", contexto)
