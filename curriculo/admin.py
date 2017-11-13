from django.contrib import admin

from .models import Curso, Disciplina, GradeCurricular, Periodo

class CursoAdmin (admin.ModelAdmin):
    list_display = ["sigla", "nome"]

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

admin.site.register(Curso,CursoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(GradeCurricular,GradeCurricularAdmin)
admin.site.register(Periodo,PeriodoAdmin)
