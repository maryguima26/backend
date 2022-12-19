from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import AlunoSerializer,DicaSerializer,ProfessorSerializer,UserSerializer,EsporteSerializer,CompeticaoSerializer,PlanoSerializer,TreinoSerializer,PerformanceSerializer,EvolucaoSerializer
from .models import Aluno,Dicas,Professor,User,Esporte,Competicao,Plano,Treino,Performance,Evolucao
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class ListUsers(APIView):
  authentication_classes=[authentication.TokenAuthentication]
  permission_classes = (permissions.IsAuthenticated,)
  def get(self,request,format=None):
    """
    Return a list of all users
    """
    user_id=[user.pk for user in User.objects.all()]
    user_name=[user.username for user in User.objects.all()]
    
    return Response(user_name)

class CustomAuthToken(ObtainAuthToken):
  def post(self,request,*args,**kwargs):
    serializer = self.serializer_class(data=request.data,context={'request':request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token,created=Token.objects.get_or_create(user=user)
    return Response({
      'token':token.key,
      'email':user.email,
      'user_id':user.pk,
      'username':user.username,
    })


  
class RegisterViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class=UserSerializer
  permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAdminUser]}
  def create(self, request, *args, **kwargs):
        return super(RegisterViewSet, self).create(request, *args, **kwargs)
  def get_permissions(self):
    try:
            # return permission_classes depending on `action` 
      return [permission() for permission in self.permission_classes_by_action[self.action]]
    except KeyError: 
            # action is not set return default permission_classes
      return [permission() for permission in self.permission_classes]

  
class AlunoViewSet(viewsets.ModelViewSet):
  queryset = Aluno.objects.all()
  serializer_class=AlunoSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,)
  filter_backends=(filters.SearchFilter,)
  search_fields=['user__username']


class ProfessorViewSet(viewsets.ModelViewSet):
  queryset = Professor.objects.all()
  serializer_class=ProfessorSerializer
  permission_classes = ()
  authentication_classes = ()

class DicaViewSet(viewsets.ModelViewSet):
  queryset = Dicas.objects.all()
  serializer_class=DicaSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,)
  filter_backends=(filters.SearchFilter,)
  search_fields=['aluno__id']

class EsporteViewSet(viewsets.ModelViewSet):
  queryset = Esporte.objects.all()
  serializer_class=EsporteSerializer
  permission_classes = ()
  authentication_classes = ()
  filter_backends=(filters.SearchFilter,)
  search_fields=['nome']


class CompeticaoViewSet(viewsets.ModelViewSet):
  queryset = Competicao.objects.all()
  serializer_class=CompeticaoSerializer
  permission_classes = ()
  authentication_classes = ()

class PlanoViewSet(viewsets.ModelViewSet):
  queryset = Plano.objects.all()
  serializer_class=PlanoSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,)
  filter_backends=(filters.SearchFilter,)
  search_fields=['aluno__nome']

class TreinoViewSet(viewsets.ModelViewSet):
  queryset = Treino.objects.all()
  serializer_class=TreinoSerializer
  permission_classes = ()
  authentication_classes = ()
  filter_backends=(filters.SearchFilter,)
  search_fields=['plano__aluno__nome','dia']

class PerformanceViewSet(viewsets.ModelViewSet):
  queryset = Performance.objects.all()
  serializer_class=PerformanceSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,)
  filter_backends=(filters.SearchFilter,)
  search_fields=['aluno__id']

class EvolucaoViewSet(viewsets.ModelViewSet):
  queryset = Evolucao.objects.all()
  serializer_class=EvolucaoSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,)
  filter_backends=(filters.SearchFilter,)
  search_fields=['aluno__id']