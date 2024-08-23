from django.contrib import admin
from django.urls import path, include
from compras.views import FornecedorViewSet, ProdutoViewSet, Pedido_comprasViewSet, Item_pedido_comprasViewSet, EstoqueViewSet, Doc_entradaViewSet
from common.views import EnderecoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fornecedor', FornecedorViewSet, basename='Fornecedores')
router.register('produto', ProdutoViewSet, basename='Produtos')
router.register('pedido_compras', Pedido_comprasViewSet, basename='Pedidos_Compras')
router.register('item_pedido_compras', Item_pedido_comprasViewSet, basename='Itens_pedidos_compras')
router.register('estoque', EstoqueViewSet, basename='Estoques')
router.register('endereco', EnderecoViewSet, basename='Enderecos')
router.register('doc_entrada', Doc_entradaViewSet, basename='Doc_entrada')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
