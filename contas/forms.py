from django import forms

from .choices import PROFESSOR, ALUNO, COORDENADOR
from .models import Aluno, Professor, Coordenador

class AlunoForm(forms.ModelForm):

    def save(self, commit=True):
        aluno = super(AlunoForm,self).save(commit=False)
        aluno.set_password("123@mudar")
        aluno.perfil = ALUNO
        if commit:
            aluno.save()
        return aluno

    class Meta:
        model = Aluno
        fields = ["ra", "nome", "email", "curso"]

class AlunoAlterarForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ["nome", "email", "curso"]

class ProfessorForm(forms.ModelForm):

    def save(self, commit=True):
        professor = super(ProfessorForm,self).save(commit=False)
        professor.set_password("mudar@123")
        professor.perfil = PROFESSOR
        if commit:
            professor.save()
        return professor

    class Meta:
        model = Professor
        fields = ["ra", "nome", "email", "apelido"]

class ProfessorAlterarForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ["nome", "email", "apelido"]

class CoordenadorForm(forms.ModelForm):

    def save(self, commit=True):
        coordenador = super(CoordenadorForm,self).save(commit=False)
        coordenador.set_password("123@mudar")
        coordenador.perfil = COORDENADOR
        if commit:
            coordenador.save()
        return coordenador

    class Meta:
        model = Coordenador
        fields = ["ra", "nome", "email", "sala"]

class CoordenadorAlterarForm(forms.ModelForm):

    class Meta:
        model = Coordenador
        fields = ["nome", "email", "sala"]