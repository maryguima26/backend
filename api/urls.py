from django.urls import path,include
from .views import AlunoViewSet,DicaViewSet,ProfessorViewSet
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register('dicas',DicaViewSet,basename='dicas')
router.register('aluno',AlunoViewSet)
router.register('professor',ProfessorViewSet)



urlpatterns=[
  path('api/',include(router.urls)),

]