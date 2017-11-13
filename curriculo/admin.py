from django.contrib import admin

from .models import Curso, Disciplina, GradeCurricular, Periodo, DisciplinaOfertada, Turma

class CursoAdmin (admin.ModelAdmin):
    list_display = ["sigla", "nome","coordenador"]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["nome","carga_horaria","teoria","pratica"]

class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ["get_sigla","ano","semestre"]
    def get_sigla(self, obj):
        return obj.curso.sigla
    get_sigla.short_description = 'Curso'
    get_sigla.admin_order_field = 'curso__sigla'

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["grade","numero","get_disciplinas"]
    raw_id_fields = ["grade"]
    def get_disciplinas(self, obj):
        return obj.disciplinas.count()
    get_disciplinas.short_description = 'Disciplinas'

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ["disciplina","ano","semestre"]
    raw_id_fields = ["disciplina"]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ["get_disciplina","identificador","turno","professor","get_alunos"]
    def get_disciplina(self, obj):
        return obj.disciplina_ofertada
    def get_alunos(self, obj):
        return obj.alunos.count()
    get_disciplina.short_description = 'Oferta'
    get_alunos.short_description = 'Alunos'

admin.site.register(Curso,CursoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(GradeCurricular,GradeCurricularAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(DisciplinaOfertada,DisciplinaOfertadaAdmin)
admin.site.register(Turma,TurmaAdmin)
