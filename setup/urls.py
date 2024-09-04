from django.contrib import admin
from django.urls import path, include
from compras.views import FornecedorViewSet, ProdutoViewSet, Pedido_comprasViewSet, Item_pedido_comprasViewSet, EstoqueViewSet, Doc_entradaViewSet
from financeiro.views import Conta_bancariaViewSet, Contas_pagarViewSet, Contas_receberViewSet, Mov_bancarioViewSet
from common.views import EnderecoViewSet
from dp_rh.views import DepartamentoViewSet, CargoViewSet, FuncionarioViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('fornecedor', FornecedorViewSet, basename='Fornecedores')
router.register('produto', ProdutoViewSet, basename='Produtos')
router.register('pedido_compras', Pedido_comprasViewSet, basename='Pedidos_Compras')
router.register('item_pedido_compras', Item_pedido_comprasViewSet, basename='Itens_pedidos_compras')
router.register('estoque', EstoqueViewSet, basename='Estoques')
router.register('endereco', EnderecoViewSet, basename='Enderecos')
router.register('doc_entrada', Doc_entradaViewSet, basename='Doc_entrada')
#--------------------------------------------------------------------------------------#
router.register('conta_bancaria', Conta_bancariaViewSet, basename='Conta_bancaria')
router.register('contas_pagar', Contas_pagarViewSet, basename='Contas_pagar')
router.register('contas_receber', Contas_receberViewSet, basename='Contas_receber')
router.register('mov_bancario', Mov_bancarioViewSet, basename='Mov_bancario')
#--------------------------------------------------------------------------------------#
router.register('departamento', DepartamentoViewSet, basename='Departamento')
router.register('cargo', CargoViewSet, basename='Cargo')
router.register('funcionario',FuncionarioViewSet, basename= 'Funcionario')
#--------------------------------------------------------------------------------------#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
