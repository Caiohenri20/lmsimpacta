from django.db import models

class Curso(models.Model):
    GRADUACAO = 'graduacao'
    POS_GRAD = 'pos-graduacao'
    TECNICO = 'tecnico'
    TIPOS = (
        (GRADUACAO, 'Graduação'),
        (POS_GRAD, 'Pós-Graduação'),
        (TECNICO, 'Técnico')
    )
    #id = models.IntegerField(blank=True, null=True)
    nome = models.CharField("Nome", unique=True, max_length=50)
    etiqueta = models.SlugField("Etiqueta", unique=True, max_length=50)
    sigla = models.CharField("Sigla", unique=True, max_length=5)
    tipo = models.CharField("Tipo", max_length=20,choices=TIPOS,default=TECNICO)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        managed = False
        db_table = 'curso'
        ordering = ['nome']

    def __str__(self):
        return self.nome