from django.contrib import admin
from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque, Doc_entrada

'''
    Estilização apresentada no acesso Admin
'''
class Fornecedores(admin.ModelAdmin):
    list_display = ('cod_forn', 'nm_fantasia', 'rz_social', 'cnpj', 'ie', 'nm_contato', 'email', 'telefone', 'status', 'end_forn')
    list_display_links = ('cod_forn', 'nm_fantasia',)
    search_fields = ('nm_fantasia',)
admin.site.register(Fornecedor, Fornecedores)
#--------------------------------------------------------------------------------------#
class Produtos(admin.ModelAdmin):
    list_display = ('cod_prod', 'descricao', 'un_medida')
    list_display_links = ('cod_prod', 'descricao',)
    search_fields = ('descricao',)
admin.site.register(Produto, Produtos)
#--------------------------------------------------------------------------------------#
class Pedidos_Compras(admin.ModelAdmin):
    list_display = ('pedido', 'emissao', 'fornecedor', 'status')
    list_display_links = ('pedido', 'fornecedor',)
    search_fields = ('pedido',)
admin.site.register(Pedido_compras, Pedidos_Compras)
#--------------------------------------------------------------------------------------#
class Itens_pedidos_compras(admin.ModelAdmin):
    list_display = ('ped_compras', 'item', 'qtd', 'preco_unitario', 'valor_total')
    list_display_links = ('ped_compras','item',)
    search_fields = ('ped_compras',)
admin.site.register(Item_pedido_compras, Itens_pedidos_compras)
#--------------------------------------------------------------------------------------#
class Estoques(admin.ModelAdmin):
    list_display = ('id', 'produto', 'saldo_est')
    list_display_links = ('id', 'produto',)
    search_fields = ('produto',)
admin.site.register(Estoque, Estoques)
#--------------------------------------------------------------------------------------#
class Docs_entradas(admin.ModelAdmin):
    list_display = ('num_nota', 'serie_nt', 'dt_emissao', 'cod_forn', 'tipo_nf', 'cond_pgto', 'forma_pgto', 'vencimento', 'item_nf_compra')
    list_display_links = ('num_nota', 'cod_forn',)
    search_fields = ('num_nota',)
admin.site.register(Doc_entrada, Docs_entradas)
#--------------------------------------------------------------------------------------#
