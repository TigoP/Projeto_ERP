from compras.views import FornecedorViewSet, ProdutoViewSet, Pedido_comprasViewSet, Item_pedido_comprasViewSet, EstoqueViewSet, Doc_entradaViewSet
from dp_rh.views import DepartamentoViewSet, CargoViewSet, FuncionarioViewSet, Vencimento_salViewSet, Desconto_salViewSet
from financeiro.views import Conta_bancariaViewSet, Contas_pagarViewSet, Contas_receberViewSet, Mov_bancarioViewSet
from common.views import EnderecoViewSet
from django.urls import path, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework import routers

class CustomRouter(DefaultRouter):
    '''
    Customização das rotas na API para ficarem separadas por setor.
    '''
    def get_api_root_view(self, api_urls=None):
        class CustomRootView(APIView):
            def get(self, request, *args, **kwargs):
                return Response({
                    'Compras': {
                        'Fornecedores': request.build_absolute_uri('fornecedor/'),
                        'Produtos': request.build_absolute_uri('produto/'),
                        'Pedidos de Compras': request.build_absolute_uri('pedido_compras/'),
                        'Itens do Pedido de Compras': request.build_absolute_uri('item_pedido_compras/'),
                        'Estoques': request.build_absolute_uri('estoque/'),
                        'Endereços': request.build_absolute_uri('endereco/'),
                        'Documentos de Entrada': request.build_absolute_uri('doc_entrada/'),
                    },
                    'Financeiro': {
                        'Contas Bancárias': request.build_absolute_uri('conta_bancaria/'),
                        'Contas a Pagar': request.build_absolute_uri('contas_pagar/'),
                        'Contas a Receber': request.build_absolute_uri('contas_receber/'),
                        'Movimentações Bancárias': request.build_absolute_uri('mov_bancario/'),
                    },
                    'Departamento Pessoal/RH': {
                        'Departamentos': request.build_absolute_uri('departamento/'),
                        'Cargos': request.build_absolute_uri('cargo/'),
                        'Funcionários': request.build_absolute_uri('funcionario/'),
                        'Vencimentos Salariais': request.build_absolute_uri('vencimento_sal/'),
                        'Descontos Salariais': request.build_absolute_uri('desconto_sal/'),
                    }
                })

        return CustomRootView.as_view()

#router = routers.DefaultRouter()
router = CustomRouter()
#Compras--------------------------------------------------------------------------------------#
router.register('fornecedor', FornecedorViewSet, basename='Fornecedores')
router.register('produto', ProdutoViewSet, basename='Produtos')
router.register('pedido_compras', Pedido_comprasViewSet, basename='Pedidos_Compras')
router.register('item_pedido_compras', Item_pedido_comprasViewSet, basename='Itens_pedidos_compras')
router.register('estoque', EstoqueViewSet, basename='Estoques')
router.register('endereco', EnderecoViewSet, basename='Enderecos')
router.register('doc_entrada', Doc_entradaViewSet, basename='Doc_entrada')
#Financeiro--------------------------------------------------------------------------------------#
router.register('conta_bancaria', Conta_bancariaViewSet, basename='Conta_bancaria')
router.register('contas_pagar', Contas_pagarViewSet, basename='Contas_pagar')
router.register('contas_receber', Contas_receberViewSet, basename='Contas_receber')
router.register('mov_bancario', Mov_bancarioViewSet, basename='Mov_bancario')
#DP-RH--------------------------------------------------------------------------------------#
router.register('departamento', DepartamentoViewSet, basename='Departamento')
router.register('cargo', CargoViewSet, basename='Cargo')
router.register('funcionario',FuncionarioViewSet, basename= 'Funcionario')
router.register('vencimento_sal', Vencimento_salViewSet, basename= 'Vencimento_sal')
router.register('desconto_sal', Desconto_salViewSet, basename= 'Desconto_sal')
#--------------------------------------------------------------------------------------#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
