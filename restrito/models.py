from django.db import models

def diretorio_questao(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'turma/{0}/questao/{1}/{2}'.format(instance.turma.id, instance.numero, filename)

class Questao(models.Model):

    turma = models.ForeignKey("curriculo.Turma")
    numero = models.SmallIntegerField("Número")
    data_limite_entrega = models.DateTimeField("Entrega")
    descricao = models.TextField("Descrição")
    data = models.DateTimeField("Início")
    arquivo = models.FileField(upload_to=diretorio_questao)

    class Meta:
        db_table = 'QUESTAO'
        unique_together = (('turma', 'numero'),)
