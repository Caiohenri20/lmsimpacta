from django.db import models

class Curso(models.Model):
    #id = models.IntegerField(primary_key=True)
    sigla = models.CharField(unique=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)
    coordenador = models.OneToOneField(
        "contas.Coordenador",
        null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'CURSO'

class Disciplina(models.Model):
    
    nome = models.CharField("Nome", unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField("Carga Horária")
    teoria = models.DecimalField("Teoria", max_digits=3, decimal_places=0, blank=True, null=True)
    pratica = models.DecimalField("Prática", max_digits=3, decimal_places=0, blank=True, null=True)
    competencias = models.TextField("Competências", blank=True, null=True)
    habilidades = models.TextField("Habilidades", blank=True, null=True)
    conteudo = models.TextField("Conteúdo", blank=True, null=True)
    bibliografia_basica = models.TextField("Bibliografia Básica", blank=True, null=True)
    bibliografia_complementar = models.TextField("Bibliografia Complementar", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'DISCIPLINA'

class GradeCurricular(models.Model):
    
    curso = models.ForeignKey(
        Curso,
        models.DO_NOTHING
    )
    ano = models.SmallIntegerField("Ano")
    semestre = models.CharField("Semestre", max_length=1)

    def __str__(self):
        return "{}-{}-{}".format(self.curso.sigla,self.ano,self.semestre)

    class Meta:
        managed = False
        db_table = 'GRADE_CURRICULAR'
        unique_together = (('ano', 'semestre', 'curso'),)
        verbose_name = "grade curricular"
        verbose_name_plural = "grades curriculares"

class Periodo(models.Model):

    grade = models.ForeignKey(
        GradeCurricular,
        models.DO_NOTHING,
        db_column="grade_curricular_id"
    )
    disciplinas = models.ManyToManyField(
        Disciplina,
        db_table="periodo_disciplina"
    )
    numero = models.SmallIntegerField("Número")

    def __str__(self):
        return "{}º de {}".format(self.numero, self.grade)

    class Meta:
        managed = False
        db_table = 'PERIODO'
        verbose_name = 'período'
        verbose_name_plural = 'períodos'
        unique_together = (('grade', 'numero'),)

class DisciplinaOfertada(models.Model):
    
    disciplina = models.ForeignKey(Disciplina)
    ano = models.SmallIntegerField("Ano")
    semestre = models.CharField("Semestre", max_length=1)

    def __str__(self):
        return "{}-{}-{}".format(self.disciplina.nome, self.ano, self.semestre)

    class Meta:
        managed = False
        db_table = 'DISCIPLINA_OFERTADA'
        verbose_name = 'oferta de disciplina'
        verbose_name_plural = 'ofertas de disciplina'
        unique_together = (('disciplina', 'ano', 'semestre'),)

class Turma(models.Model):
    
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING)
    identificador = models.CharField(max_length=1)
    turno = models.CharField(max_length=15, blank=True, null=True)
    professor = models.ForeignKey("contas.Professor", blank=True, null=True)
    alunos = models.ManyToManyField(
        "contas.Aluno",
        db_table="MATRICULA"
    )

    def __str__(self):
        return "{}-{}".format(self.disciplina_ofertada,self.identificador)

    class Meta:
        managed = False
        db_table = 'TURMA'
        unique_together = (('disciplina_ofertada', 'identificador'),)
        