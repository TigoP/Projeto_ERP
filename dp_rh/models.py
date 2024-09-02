from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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