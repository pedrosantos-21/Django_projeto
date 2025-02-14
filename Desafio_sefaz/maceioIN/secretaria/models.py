from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=50, choices=[
        ('Contabilidade', 'Contabilidade'),
        ('Financeiro', 'Financeiro'),
        ('Atendimento', 'Atendimento'),
        ('Orçamento', 'Orçamento'),
        ('TI', 'TI')
    ])
    email = models.EmailField()

    def __str__(self):
        return self.nome