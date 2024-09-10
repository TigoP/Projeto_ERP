from dp_rh.models import Departamento, Cargo, Funcionario, Vencimento_sal, Desconto_sal
from django.contrib import admin

class Departamentos(admin.ModelAdmin):
    list_display=('cod_dep', 'nm_dep', 'descricao')
    list_display_links=('cod_dep', 'nm_dep')
    list_per_page = 10
    search_fields=('nm_dep',)
    ordering = ['nm_dep']
admin.site.register(Departamento, Departamentos)
#--------------------------------------------------------------------------------------#
class Cargos(admin.ModelAdmin):
    list_display = ('cod_cargo', 'nm_funcao', 'descricao', 'sal_base', 'departamento')
    list_display_links = ('nm_funcao', 'departamento')
    list_per_page = 10
    search_fields = ('nm_funcao',)
    ordering = ['nm_funcao']
admin.site.register(Cargo, Cargos)
#--------------------------------------------------------------------------------------#
class Funcionarios(admin.ModelAdmin):
    #list_display = ('cod_funci', 'nm_funcionario', 'cpf', 'rg', 'dt_nasc', 'nacionalidade', 'estado_civil', 'sexo', 'cargo_func', 'salario', 'dt_admissao', 'depart_func', 'situacao', 'end_func')
    list_display = [field.name for field in Funcionario._meta.fields]
    list_display_links = ('nm_funcionario', 'cargo_func')
    list_per_page = 20
    search_fields = ('nm_funcionario',)
    ordering = ['nm_funcionario']
admin.site.register(Funcionario, Funcionarios)
#--------------------------------------------------------------------------------------#
class Vencimentos_sal(admin.ModelAdmin):
    list_display = [field.name for field in Vencimento_sal._meta.fields]
admin.site.register(Vencimento_sal, Vencimentos_sal)
#--------------------------------------------------------------------------------------#
class Descontos_sal(admin.ModelAdmin):
    list_display = [field.name for field in Desconto_sal._meta.fields]
admin.site.register(Desconto_sal, Descontos_sal)
#--------------------------------------------------------------------------------------#