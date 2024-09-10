from django.db.models.signals import pre_save
from django.dispatch import receiver
from common.models import Endereco
from django.db import models

'''
    Classes de cadastros a serem utilizadas nas funções.
'''
class Departamento(models.Model):
    cod_dep = models.CharField(max_length = 6, unique = True, blank = True)
    nm_dep = models.CharField(max_length = 25)
    descricao = models.TextField(max_length = 500)
    
    def __str__(self):
        return f'{self.cod_dep} - {self.nm_dep}'
    
@receiver(pre_save, sender=Departamento)
def gerar_cod_dep(sender, instance, **kwargs):
    if not instance.cod_dep:
        ultimo_cod = Departamento.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.cod_dep) + 1
            instance.cod_dep = f'{novo_cod:06d}'
        else:
            instance.cod_dep = '000001'
#--------------------------------------------------------------------------------------#
class Cargo(models.Model):
    cod_cargo = models.CharField(max_length = 6, unique = True, blank = True)
    nm_funcao = models.CharField(max_length = 25)
    descricao = models.CharField(max_length= 50)
    sal_base = models.DecimalField(max_digits= 10, decimal_places=2)
    departamento = models.ForeignKey(Departamento, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.cod_cargo} - {self.nm_funcao}'

@receiver(pre_save, sender=Cargo)
def gerar_cod_cargo(sender, instance, **kwargs):
    if not instance.cod_cargo:
        ultimo_cod = Cargo.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.cod_cargo) + 1
            instance.cod_cargo = f'{novo_cod:06d}'
        else:
            instance.cod_cargo = '000001'
#--------------------------------------------------------------------------------------#
class Funcionario(models.Model):
    SITUACAO = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    CIVIL = (
        ('C', 'Casado'),
        ('S', 'Solteiro'),
        ('V', 'Viuvo'),
        ('D', 'Disquitado'),
    )
    cod_funci = models.CharField(max_length= 6, unique= True, blank= True)
    nm_funcionario = models.CharField(max_length= 30)
    cpf = models.CharField(max_length= 11)
    rg = models.CharField(max_length= 10)
    dt_nasc = models.DateField()
    nacionalidade = models.CharField(max_length= 15)
    estado_civil = models.CharField(max_length= 1, choices=CIVIL, blank= False, default= 'S')
    dependentes = models.IntegerField()
    sexo = models.CharField(max_length= 1, choices= SEXO, blank= False, default= "M")
    cargo_func = models.ForeignKey(Cargo, on_delete= models.CASCADE)
    salario = models.DecimalField(Cargo.sal_base, max_digits=10, decimal_places= 2)
    dt_admissao = models.DateField()
    depart_func = models.ForeignKey(Departamento, on_delete= models.CASCADE)
    situacao = models.CharField(max_length= 1, choices=SITUACAO, blank=False, default= "A")
    end_func = models.ForeignKey(Endereco, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.nm_funcionario} - {self.cargo_func}'
    
@receiver(pre_save, sender= Funcionario)
def gerar_cod_funci(sender, instance, **Kwargs):
    if not instance.cod_funci:
        ultimo_cod = Funcionario.objects.all().order_by('id').last()
        if ultimo_cod:
            novo_cod = int(ultimo_cod.cod_funci) + 1
            instance.cod_funci = f'{novo_cod:06d}'
        else:
            instance.cod_funci = '000001'
#--------------------------------------------------------------------------------------#
class Vencimento_sal(models.Model):
    sal_base = models.ForeignKey(Cargo, on_delete= models.CASCADE)

    Comissao = models.DecimalField (max_digits=10, decimal_places=2)
    qtd_hora_extra50 = models.IntegerField()
    qtd_hora_extra100 = models.IntegerField()
    hora_extra = models.DecimalField (max_digits=10, decimal_places=2)
    qtd_ad_noturno = models.IntegerField()
    ad_noturno = models.DecimalField (max_digits=10, decimal_places=2)
    sal_familia = models.DecimalField (max_digits=10, decimal_places=2)
    adiantamentoV = models.DecimalField (max_digits=10, decimal_places=2)
    gratificacao = models.DecimalField (max_digits=10, decimal_places=2)
    emprestimoV = models.DecimalField (max_digits=10, decimal_places=2)
    total_vencimentos = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.funcionario} - Vencimentos: R${self.total_vencimentos}'
#--------------------------------------------------------------------------------------#
class Desconto_sal(models.Model):
    sal_base = models.ForeignKey(Cargo, on_delete= models.CASCADE)

    inss = models.DecimalField (max_digits=10, decimal_places=2)
    fgts = models.DecimalField (max_digits=10, decimal_places=2)
    pensao = models.DecimalField (max_digits=10, decimal_places=2)
    irrf = models.DecimalField (max_digits=10, decimal_places=2)
    transporte = models.DecimalField (max_digits=10, decimal_places=2)
    alimentacao = models.DecimalField (max_digits=10, decimal_places=2)
    atrasos = models.DecimalField (max_digits=10, decimal_places=2)
    qtd_faltas = models.IntegerField()
    faltas = models.DecimalField (max_digits=10, decimal_places=2)
    adiantamentoD = models.DecimalField (max_digits=10, decimal_places=2)
    plano_saude = models.DecimalField (max_digits=10, decimal_places=2)
    plano_odonto = models.DecimalField (max_digits=10, decimal_places=2)
    emprestimoD = models.DecimalField (max_digits=10, decimal_places=2)
    total_descontos = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.funcionario} - Descontos: R${self.total_descontos}'
#--------------------------------------------------------------------------------------#
