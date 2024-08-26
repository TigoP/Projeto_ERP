from django.contrib import admin
from financeiro.views import Conta_bancaria, Contas_pagar, Contas_receber, Mov_bancario

class Contas_bancarias(admin.ModelAdmin):
    list_display = ('nome', 'num_conta', 'saldo_conta')
    list_display_links = ('nome','num_conta',)
    search_fields = ('num_conta',)
admin.site.register(Conta_bancaria, Contas_bancarias)
#--------------------------------------------------------------------------------------#
class Contas_pagars(admin.ModelAdmin):
    list_display = ('documento', 'descricao', 'valor', 'data_vencimento', 'status', 'fornecedor')
    list_display_links = ('documento', 'valor',)
    search_fields = ('documento',)
admin.site.register(Contas_pagar, Contas_pagars)
#--------------------------------------------------------------------------------------#
class Contas_recebers(admin.ModelAdmin):
    list_display = ('documento', 'descricao', 'valor', 'data_vencimento', 'status', 'cliente')
    list_display_links = ('documento', 'valor',)
    search_fields = ('documento',)
admin.site.register(Contas_receber, Contas_recebers)
#--------------------------------------------------------------------------------------#
class Mov_bancarios(admin.ModelAdmin):
    list_display = ('dt_inicio', 'dt_fim', 'conta_bancaria', 'entradas', 'saidas', 'saldo_periodo')
    list_display_links = ('conta_bancaria', 'saldo_periodo',)
    search_fields = ('conta_bancaria',)
admin.site.register(Mov_bancario, Mov_bancarios)
#--------------------------------------------------------------------------------------#
