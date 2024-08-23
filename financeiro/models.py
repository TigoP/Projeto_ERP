from django.db import models
from compras.serializers import Doc_entradaSerializer

'''class Conta_bancaria(models.Model):
    BANCOS = (
        ('001', 'Banco do Brasil S.A.'),
        ('021', 'Banestes S.A.'),
    )
    nome = models.CharField(max_length=3, choices=BANCOS, blank=False, default='')
    num_conta = models.IntegerField()
    saldo_conta = models.DecimalField(max_digits==10)
#--------------------------------------------------------------------------------------#
class contas_pagar(models.Model):
    documento = models.ForeignKey(Doc_entradaSerializer, related_name='num_nota', on_delete=models.CASCADE)
    vlr_total = models.ForeignKey(Doc_entradaSerializer, related_name='valor_total', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Doc_entradaSerializer, related_name='cod_forn', on_delete=models.CASCADE)'''
