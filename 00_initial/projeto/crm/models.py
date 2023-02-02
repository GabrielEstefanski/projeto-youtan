from django.db import models

class Empresa(models.Model):

    STATUS = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo')
    )
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField(max_length=50)
    ativo = models.CharField(
        max_length=7,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Cnpj(models.Model):
    cnpj = models.CharField(max_length=50, verbose_name="CNPJ")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    
    def __str__(self) -> str:
        return self.cnpj
