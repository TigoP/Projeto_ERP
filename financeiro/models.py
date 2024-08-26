from django.db import models
from compras.models import Doc_entrada, Fornecedor

class Conta_bancaria(models.Model):
    BANCOS = (
        ('001', 'Banco do Brasil S.A.'),
        ('021', 'Banestes S.A.'),
    )
    nome = models.CharField(max_length=3, choices=BANCOS, blank=False, default='')
    num_conta = models.IntegerField()
    saldo_conta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Saldo da conta {self.nome} é {self.saldo_conta}'
#--------------------------------------------------------------------------------------#
class Contas_pagar(models.Model):
    documento = models.ForeignKey(Doc_entrada, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=20, default='Pendente')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Valor a pagar de {self.fornecedor.rz_social} referente ao documento {self.documento.num_nota}'
    
class Contas_receber(models.Model):
    documento = models.CharField(max_length=10) #forenkey NF saida
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=20,default='Pendente')
    cliente = models.CharField(max_length=6) #forenkey cliente

    #def __str__(self):
    #    return f'Valor a receber de {self.cliente.rz_social} referente ao documento {self.documento.num_nota}'

class Mov_bancario(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    conta_bancaria = models.ForeignKey(Conta_bancaria, on_delete=models.CASCADE, default=1)
    entradas = models.DecimalField(max_digits=10, decimal_places=2, default=1) #forenkey fornecedor
    saidas = models.DecimalField(max_digits=10, decimal_places=2, default=1) #forenkey cliente
    saldo_periodo = models.DecimalField(max_digits=10, decimal_places=2, default=1) #regra de 1 menos outro

    def __str__(self):
        return f'Saldo da conta: {self.saldo_periodo}'
