from django.db.models.signals import pre_save
from django.dispatch import receiver
from common.models import Endereco
from django.db import models

'''
    Classes de cadastros a serem utilizadas nas funções.
'''

class Fornecedor(models.Model):
    STATUS = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )

    cod_forn = models.CharField(max_length = 6, unique = True, blank = True)
    nm_fantasia = models.CharField(max_length=150)
    rz_social = models.CharField(max_length=150)
    end_forn = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=11, null=True) 
    nm_contato = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=16)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, default='A')

    def __str__(self):
        return f'{self.cod_forn} - {self.rz_social}'
    
@receiver(pre_save, sender=Fornecedor)
def gerar_cod_forn(sender, instance, **kwargs):
    if not instance.cod_forn:
        ultimo_cod = Fornecedor.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.cod_forn) + 1
            instance.cod_forn = f'{novo_cod:06d}'
        else:
            instance.cod_forn = '000001'
#--------------------------------------------------------------------------------------#
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
    cod_prod = models.CharField(max_length=6, unique=True)
    descricao = models.TextField(max_length=100)
    un_medida = models.CharField(max_length=2, choices=MEDIDA, blank=False, default='UN')

    def __str__(self):
        return f'{self.cod_prod} - {self.descricao}'

@receiver(pre_save, sender=Produto)
def gerar_cod_prod(sender, instance, **kwargs):
    if not instance.cod_prod:
        ultimo_cod = Produto.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.cod_prod) + 1
            instance.cod_prod = f'{novo_cod:06d}'
        else:
            instance.cod_prod = '000001'
#--------------------------------------------------------------------------------------#    
'''
    Criação de atividades que utilizarão os cadastros criados.
'''

class Pedido_compras(models.Model):
    STATUS = (
        ('A', 'Aberto'),
        ('F', 'Fechado'),
    )
    pedido = models.CharField(max_length=6)
    emissao = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices= STATUS, blank=False, default='A')

    def __str__(self):
        return f'Pedido {self.pedido} - {self.fornecedor.nm_fantasia}' 

@receiver(pre_save, sender=Pedido_compras)
def gerar_pedido(sender, instance, **kwargs):
    if not instance.pedido:
        ultimo_cod = Pedido_compras.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.pedido) + 1
            instance.pedido = f'{novo_cod:06d}'
        else:
            instance.pedido = '000001'
#--------------------------------------------------------------------------------------#
class Item_pedido_compras(models.Model):
    ped_compras = models.ForeignKey(Pedido_compras, related_name='item', on_delete=models.CASCADE) 
    item = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.PositiveIntegerField(null=False, blank=False)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False) 

    def save(self, *args, **kwargs): 
        '''
        Função que sobrescreve o save do PC usando a função calcular total, calcula e salva e chama o save da classe pai
        '''
        self.valor_total = self.calcular_vlr_total() 
        super().save(*args, **kwargs) 

    def calcular_vlr_total(self): 
        return self.qtd * self.preco_unitario 
    
    def __str__(self):
        return f'{self.qtd} x {self.item.descricao}'
#--------------------------------------------------------------------------------------#    
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    saldo_est = models.FloatField()

    def adicionar_estoque(self, qtd):
        self.saldo_est += qtd
        self.save()

    def reduzir_estoque(self, quantidade):
        self.saldo_est -= quantidade
        self.save()

    def verificar_disponibilidade(self):
        return self.saldo_est > 0

    def __str__(self):
        return f'{self.produto.descricao} - {self.saldo_est} em estoque' 
#--------------------------------------------------------------------------------------#    
class Doc_entrada(models.Model):
    ESPECIE = (
        ('NFE', 'NF-e'),
        ('NFS', 'NFS'),
        ('CTE', 'CT-e'),
    )
    CONDICAO = (
        ('001', 'A vista'),
        ('002', '7 dias'),
        ('003', '30 dias'),
        ('020', '30,60'),
        ('021', '30,60,90'),
    )
    FORMA = (
        ('R$', 'Dinheiro'),
        ('PIX', 'Pix'),
        ('CD', 'Cartao Debito'),
        ('CC', 'Cartao Credito'),
    )
    num_nota = models.IntegerField()
    serie_nt = models.CharField(max_length=3)
    dt_emissao = models.DateField()
    cod_forn = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    tipo_nf = models.CharField(max_length=3, choices=ESPECIE, blank=False, default='')
    cond_pgto = models.CharField(max_length=3, choices=CONDICAO, blank=False, default='')
    forma_pgto = models.CharField(max_length=3, choices=FORMA, blank=False, default='')
    vencimento = models.DateField()
    item_nf_compra = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_item = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    def calcular_vlr_total(self): 
        return self.qtd_item * self.preco_unitario

    def __str__(self):
        return f'{self.num_nota} - {self.tipo_nf} - {self.cod_forn.rz_social}'
#--------------------------------------------------------------------------------------#
