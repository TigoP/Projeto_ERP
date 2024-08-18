from django.db import models
from common.models import Endereco

class Fornecedor(models.Model):
    cod_forn = models.AutoField(primary_key=True)
    nm_fantasia = models.CharField(max_length=150)
    rz_social = models.CharField(max_length=150)
    end_forn = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    nm_contato = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=16)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nm_fantasia

class Produto(models.Model):
    MEDIDA = (
        ('UN', 'Unidade'),
        ('G', 'Grama'),    
        ('KG', 'Quilo'),
        ('T', 'Tonelada'),
        ('L', 'Litro'),
        ('CM', 'Centímetro'),
        ('M', 'Metro'),
    )
    cod_prod = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=100)
    un_medida = models.CharField(max_length=2, choices=MEDIDA, blank=False, default='UN')

    def __str__(self):
        return self.cod_prod
    
class Pedido_compras(models.Model):
    STATUS = (
        ('A', 'Aberto'),
        ('F', 'Fechado')
    )
    pedido = models.AutoField(primary_key=True)
    emissao = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices= STATUS, blank=False, default='A')

    def __str__(self):
        return self.pedido

class Item_pedido_compras(models.Model):
    ped_compras = models.ForeignKey(Pedido_compras, on_delete=models.CASCADE)
    item = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.PositiveIntegerField(null=False, blank=False)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item
    
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    saldo_est = models.FloatField(max_length=10)

    def __str__(self):
        return self.saldo_est
    