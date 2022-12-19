# from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Aluno,Professor,Dicas,User, Esporte,Competicao,Plano,Treino,Performance,Evolucao
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =['id','username','email','password','is_aluno','is_professor']

    extra_kwargs = {
      'password':{
      'write_only': True,
      'required': True
    }
    }
  
  def validated_username(self,value):
    if User.objects.filter(username__iexact=value).exists():
      raise serializers.ValidationError("Um usuário com esse nome já existe. Escolha outro nome de usuário")
    return value 
  def create(self,validated_data):
    user = User.objects.create_user( 
      username=validated_data["username"],
      password=validated_data["password"],
      is_aluno=validated_data["is_aluno"],
      is_professor=validated_data["is_professor"]
    )
    if user is not None:
      try:
        token=Token.objects.get(user_id=user.id)
      except Token.DoesNotExist:
        token = Token.objects.create(user=user)
    return user

    
  
class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = ['id','user','nome','email','sexo','peso','altura','idade','nivel','esporte']

class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Professor
    fields = ['id','nome','email']


class DicaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dicas
    fields = ['id','description','aluno']


class DicaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dicas
    fields = ['id','description','aluno','evolucao']


class EsporteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Esporte
    fields = ['id','nome']

class CompeticaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Competicao
    fields = ['id','nome','esporte','data']

class PlanoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plano
    fields = ['id','aluno','competicao']

class TreinoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Treino
    fields = ['id','descricao','plano','dia']

class PerformanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Performance
    fields = ['id','aluno','tempo','quilometragem','esforco','treino']

class EvolucaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Evolucao
    fields = ['id','aluno','descricao','treino']
