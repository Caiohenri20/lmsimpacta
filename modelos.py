# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class CursoTurma(models.Model):
    curso = models.ForeignKey(Curso, models.DO_NOTHING, primary_key=True)
    turma = models.ForeignKey('Turma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CURSO_TURMA'
        unique_together = (('curso', 'turma'),)


class DisciplinaOfertada(models.Model):
    id = models.IntegerField(primary_key=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'DISCIPLINA_OFERTADA'
        unique_together = (('disciplina', 'ano', 'semestre'),)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, models.DO_NOTHING, primary_key=True)
    turma = models.ForeignKey('Turma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MATRICULA'
        unique_together = (('aluno', 'turma'),)


class Periodo(models.Model):
    id = models.IntegerField(primary_key=True)
    grade_curricular = models.ForeignKey(GradeCurricular, models.DO_NOTHING)
    numero = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'PERIODO'
        unique_together = (('grade_curricular', 'numero'),)


class PeriodoDisciplina(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING, primary_key=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PERIODO_DISCIPLINA'
        unique_together = (('periodo', 'disciplina'),)


class Turma(models.Model):
    id = models.IntegerField(primary_key=True)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING)
    identificador = models.CharField(max_length=1)
    turno = models.CharField(max_length=15, blank=True, null=True)
    professor = models.ForeignKey(Professor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TURMA'
        unique_together = (('disciplina_ofertada', 'identificador'),)



