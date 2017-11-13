# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UsuarioManager
from .choices import PERFIS

class Usuario(AbstractBaseUser):

    ra = models.IntegerField("RA", unique=True)
    nome = models.CharField("Nome", max_length=150)
    email = models.EmailField("E-Mail", max_length=50)
    celular = models.CharField("Celular", max_length=11, blank=True, null=True)
    ativo = models.BooleanField("Ativo", default=True)
    perfil = models.CharField("Perfil", max_length=1, choices=PERFIS)

    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "ra"
    REQUIRED_FIELDS = ["email","nome"]

    objects = UsuarioManager()

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def __str__(self):
        return self.nome

    @property
    def is_staff(self):
        return self.perfil == "C"

    def has_module_perms(self, package_name):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    class Meta:
        db_table = 'USUARIO'

class Aluno(Usuario):

    parent_link = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column="usuario_id",
        parent_link=True
    )
    curso = models.OneToOneField('curriculo.Curso')

    class Meta:
        managed = False
        db_table = 'ALUNO'

class Professor(Usuario):
    parent_link = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column="usuario_id",
        parent_link=True
    )
    apelido = models.CharField("Apelido", unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'PROFESSOR'
        verbose_name = "professor"
        verbose_name_plural = "professores"