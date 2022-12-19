from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
  is_aluno=models.BooleanField(default=False)
  is_professor=models.BooleanField(default=False)
  def __str__(self):
    return self.username
  

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
  if created: 
    Token.objects.create(user=instance)


class Esporte(models.Model):
  nome = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.nome}"

class Aluno(models.Model):
  user    = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  nome    = models.CharField(max_length=100)
  email   = models.EmailField(max_length=254)
  sexo    = models.CharField(max_length=2)
  peso    = models.FloatField()
  altura  = models.IntegerField()
  idade   = models.IntegerField()
  nivel   = models.IntegerField()
  esporte = models.OneToOneField(Esporte,on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.nome}"
 


class Professor(models.Model):
  user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  nome = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  
  def __str__(self):
    return f"{self.nome}"





class Competicao(models.Model):
  nome = models.CharField(max_length=100)
  esporte = models.OneToOneField(Esporte, on_delete=models.CASCADE)
  data = models.DateField()

  def __str__(self):
    return f"{self.nome}:{self.data}"



class Plano(models.Model):
  descricao = models.CharField(max_length=100)
  aluno = models.OneToOneField(Aluno,on_delete=models.CASCADE)
  competicao = models.OneToOneField(Competicao,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.aluno}:{self.descricao}"

class Treino(models.Model):
  descricao = models.TextField()
  plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
  dia = models.DateField()

  def __str__(self):
    return f"{self.dia}"

class Performance(models.Model):
  aluno=models.ForeignKey(Aluno, on_delete=models.CASCADE)
  tempo = models.IntegerField()
  quilometragem = models.IntegerField()
  esforco = models.CharField(max_length=20)
  treino = models.OneToOneField(Treino, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.treino}"

class Evolucao(models.Model):
  aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=100)
  treino = models.OneToOneField(Treino, on_delete = models.PROTECT)
  
  def __str__ (self):
    return f"{self.aluno}:{self.descricao}"

class Dicas(models.Model):
  description = models.TextField()
  aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
  evolucao = models.OneToOneField(Evolucao, on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return f"{self.aluno}"





 

