from django.contrib import admin
from dp_rh.models import Departamento, Cargo, Funcionario

class Departamentos(admin.ModelAdmin):
    list_display=('cod_dep', 'nm_dep', 'descricao')
    list_display_links=('cod_dep', 'nm_dep')
    search_fields=('nm_dep',)
admin.site.register(Departamento, Departamentos)
#--------------------------------------------------------------------------------------#
class Cargos(admin.ModelAdmin):
    list_display = ('cod_cargo', 'nm_funcao', 'descricao', 'sal_base', 'departamento')
    list_display_links = ('nm_funcao', 'departamento')
    search_fields = ('nm_funcao',)
admin.site.register(Cargo, Cargos)
#--------------------------------------------------------------------------------------#
class Funcionarios(admin.ModelAdmin):
    #list_display = ('cod_funci', 'nm_funcionario', 'cpf', 'rg', 'dt_nasc', 'nacionalidade', 'estado_civil', 'sexo', 'cargo_func', 'salario', 'dt_admissao', 'depart_func', 'situacao', 'end_func')
    list_display = [field.name for field in Funcionario._meta.fields]
    list_display_links = ('nm_funcionario', 'cargo_func')
    search_fields = ('nm_funcionario',)
admin.site.register(Funcionario, Funcionarios)
#--------------------------------------------------------------------------------------#