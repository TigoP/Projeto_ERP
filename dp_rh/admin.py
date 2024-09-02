from django.contrib import admin
from dp_rh.models import Departamento, Cargo

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