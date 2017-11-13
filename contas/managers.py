from django.contrib.auth.models import BaseUserManager
from .choices import COORDENADOR


class UsuarioManager(BaseUserManager):

    def _criar_usuario(self, ra, password, **campos):
        if not ra: 
            raise ValueError("RA deve ser declarado!")
        user = self.model(ra=ra, **campos)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **campos):
        return self._criar_usuario(ra, password, **campos)

    def create_superuser(self, ra, password=None, **campos):
        campos.setdefault('perfil', COORDENADOR)
        return self._criar_usuario(ra, password, **campos)


