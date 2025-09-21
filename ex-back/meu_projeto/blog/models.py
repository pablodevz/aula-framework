from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Ex: SP, RJ, etc.
    cep = models.CharField(max_length=9)     # Ex: 00000-000

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"
    
class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome