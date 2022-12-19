from django.contrib import admin
from .models import Aluno,Dicas,Professor,User,Esporte,Performance,Competicao,Plano,Treino,Evolucao


# Register your models here.
@admin.register(User)
class UserModel(admin.ModelAdmin):
  list_filter=('username','password','is_aluno','is_professor')
  list_display=('username','password','is_aluno','is_professor')

@admin.register(Aluno)
class AlunoModel(admin.ModelAdmin):
  list_filter=('nome','email')
  list_display=('nome','email')

@admin.register(Dicas)
class DicaModel(admin.ModelAdmin):
  list_filter=('description','aluno','evolucao')
  list_display=('description','aluno','evolucao')

@admin.register(Professor)
class ProfessorModel(admin.ModelAdmin):
  list_filter=('nome','email')
  list_display=('nome','email')

@admin.register(Esporte)
class EsporteModel(admin.ModelAdmin):
  list_filter=('nome',)
  list_display=('nome',)

@admin.register(Competicao)
class CompeticaoModel(admin.ModelAdmin):
  list_filter=('nome','esporte','data')
  list_display=('nome','esporte','data')

@admin.register(Plano)
class PlanoModel(admin.ModelAdmin):
  list_filter=('aluno','competicao')
  list_display=('aluno','competicao')


@admin.register(Treino)
class TreinoModel(admin.ModelAdmin):
  list_filter=('descricao','plano','dia')
  list_display=('descricao','plano','dia')

@admin.register(Performance)
class PerformanceModel(admin.ModelAdmin):
  list_filter=('aluno','tempo','quilometragem','esforco','treino')
  list_display=('aluno','tempo','quilometragem','esforco','treino')

@admin.register(Evolucao)
class EvolucaoModel(admin.ModelAdmin):
  list_filter=('aluno','descricao','treino')
  list_display=('aluno','descricao','treino')



