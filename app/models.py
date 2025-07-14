from django.db import models

# Create your models here.
from django.db.models.functions import Now
class questionario(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Nome do questionario", default=f"Questionario_{Now()}")    
    freq = models.CharField(max_length=50)
    dat_cria = models.DateTimeField(verbose_name="data de cadastro", auto_now_add=True)
    ativo = models.BooleanField(verbose_name="ativo")
    
    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "questionario"
        verbose_name_plural = "questionarios"

class tipoPergunta(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Tipo de Pergunta")
    descricao = models.TextField(verbose_name="Descricao", blank=True, null=True)

    class Meta:
        verbose_name = "tipopergunta"
        verbose_name_plural = "tipoperguntas"

    def __str__(self):
        return self.nome

class pergunta(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Pergunta")
    descricao = models.TextField(verbose_name="Descricao", blank=True, null=True)
    tipo = models.ForeignKey(tipoPergunta, on_delete=models.CASCADE, verbose_name="Tipo de Pergunta")
    dat_cria = models.DateTimeField(verbose_name="data de cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "pergunta"
        verbose_name_plural = "perguntas"

    def __str__(self):
        return {self.nome}

class funcao(models.Model):

    nome = models.CharField(verbose_name='funcao', max_length=50)


    class Meta:
        verbose_name = "funcao"
        verbose_name_plural = "funcoes"

    def __str__(self):
        return self.nome

class usuario(models.Model):

    nome = models.CharField(verbose_name='nome', max_length=50)
    contato = models.CharField(verbose_name='contato', max_length=50)
    funcao = models.ForeignKey(funcao, on_delete=models.CASCADE, verbose_name='funcao')
    dat_cadastro = models.DateTimeField(verbose_name="data de cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.nome

class resposta(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Nome da Resposta", default=f"Resposta_{Now()}")
    resposta = models.CharField(max_length=100, verbose_name="Resposta")
    pergunta = models.ForeignKey(pergunta, on_delete=models.CASCADE, verbose_name="Pergunta")
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    dat_cria = models.DateTimeField(verbose_name="data de cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "resposta"
        verbose_name_plural = "respostas"

    def __str__(self):
        return self.nome

class questionarioPergunta(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nome da Pergunta", default=f"Pergunta_{Now()}")
    questionario = models.ForeignKey(questionario, on_delete=models.CASCADE, verbose_name="Questionario")
    pergunta = models.ForeignKey(pergunta, on_delete=models.CASCADE, verbose_name="Pergunta")    

    class Meta:
        verbose_name = "questionariopergunta"
        verbose_name_plural = "questionarioperguntas"

    def __str__(self):
        return self.name