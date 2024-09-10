from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque, Doc_entrada
from django.contrib import admin

'''
    Estilização apresentada no acesso Admin
'''
class Fornecedores(admin.ModelAdmin):
    list_display = ('cod_forn', 'nm_fantasia', 'rz_social', 'cnpj', 'ie', 'nm_contato', 'email', 'telefone', 'status', 'end_forn')
    list_display_links = ('cod_forn', 'nm_fantasia',)
    list_per_page = 10
    search_fields = ('nm_fantasia',)
    ordering = ['cod_forn']
admin.site.register(Fornecedor, Fornecedores)
#--------------------------------------------------------------------------------------#
class Produtos(admin.ModelAdmin):
    list_display = ('cod_prod', 'descricao', 'un_medida')
    list_display_links = ('cod_prod', 'descricao',)
    list_per_page = 10
    search_fields = ('descricao',)
    ordering = ['cod_prod']
admin.site.register(Produto, Produtos)
#--------------------------------------------------------------------------------------#
class Pedidos_Compras(admin.ModelAdmin):
    list_display = ('pedido', 'emissao', 'fornecedor', 'status')
    list_display_links = ('pedido', 'fornecedor',)
    list_per_page = 10
    search_fields = ('pedido',)
    ordering = ['pedido']
admin.site.register(Pedido_compras, Pedidos_Compras)
#--------------------------------------------------------------------------------------#
class Itens_pedidos_compras(admin.ModelAdmin):
    list_display = ('ped_compras', 'item', 'qtd', 'preco_unitario', 'valor_total')
    list_display_links = ('ped_compras','item',)
    list_per_page = 10
    search_fields = ('ped_compras',)
    ordering = ['ped_compras']
admin.site.register(Item_pedido_compras, Itens_pedidos_compras)
#--------------------------------------------------------------------------------------#
class Estoques(admin.ModelAdmin):
    list_display = ('id', 'produto', 'saldo_est')
    list_display_links = ('id', 'produto',)
    list_per_page = 10
    search_fields = ('produto',)
    ordering = ['produto']
admin.site.register(Estoque, Estoques)
#--------------------------------------------------------------------------------------#
class Docs_entradas(admin.ModelAdmin):
    list_display = ('num_nota', 'serie_nt', 'dt_emissao', 'cod_forn', 'tipo_nf', 'cond_pgto', 'forma_pgto', 'vencimento', 'item_nf_compra')
    list_display_links = ('num_nota', 'cod_forn',)
    list_per_page = 10
    search_fields = ('num_nota',)
    ordering = ['num_nota']
admin.site.register(Doc_entrada, Docs_entradas)
#--------------------------------------------------------------------------------------#
