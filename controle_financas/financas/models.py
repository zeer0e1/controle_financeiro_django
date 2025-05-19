from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=1,
        choices=[
            ('R','Receita'),
            ('D','Despesas')
        ]
    )

    def __str__(self):
        return self.nome
    

class Conta(models.Model):
    nome_conta = models.CharField(max_length=100)
    valor_atual = models.DecimalField(max_digits=10, decimal_places=2)
    nome_banco = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_conta
    

class Transacao(models.Model):
    tipo = models.CharField(
        max_length=1,
        choices=[
            ('R','Receita'),
            ('D','Despesas')
        ]
    )

    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.get_tipo_display()} -  {self.descricao} - {self.valor}'