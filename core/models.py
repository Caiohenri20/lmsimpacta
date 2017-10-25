from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class UsuarioManager(BaseUserManager):

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA é obrigatório')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        extra_fields.setdefault('superuser', False)
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        extra_fields.setdefault('superuser', True)
        extra_fields.setdefault('equipe', True)
        extra_fields.setdefault('perfil', "Admin")
        return self._create_user(ra, password, **extra_fields)

# Create your models here.
class Usuario(AbstractBaseUser):
    ra = models.BigIntegerField('RA', unique=True)
    email = models.CharField('E-Mail',max_length=50, blank=True, null=True)
    primeiro_nome = models.CharField('Primeiro Nome',max_length=50, blank=True, null=True)
    ultimo_nome = models.CharField('Último Nome',max_length=50, blank=True, null=True)

    perfil = models.CharField('Perfil', max_length=50, blank=True, null=True)

    ativo = models.BooleanField('Ativo', default=True)
    superuser = models.BooleanField('Admin', default=False)
    equipe = models.BooleanField('Equipe', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_full_name(self):
        full_name = '%s %s' % (self.primeiro_nome, self.ultimo_nome)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.primeiro_nome

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.equipe