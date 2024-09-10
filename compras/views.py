from compras.serializers import FornecedorSerializer, ProdutoSerializer, Pedido_comprasSerializer, Item_pedido_comprasSerializer, EstoqueSerializer, Doc_entradaSerializer
from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque, Doc_entrada
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['cod_forn']
    search_fields = ['nm_fantasia', 'cnpj']
#--------------------------------------------------------------------------------------#
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['cod_prod']
    search_fields = ['cod_prod', 'descricao']
#--------------------------------------------------------------------------------------#
class Pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Pedido_compras.objects.all()
    serializer_class = Pedido_comprasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['pedido']
    search_fields = ['pedido', 'fornecedor']

    def create_pedido(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response
#--------------------------------------------------------------------------------------#
class Item_pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Item_pedido_compras.objects.all()
    serializer_class = Item_pedido_comprasSerializer
#--------------------------------------------------------------------------------------#
class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
#--------------------------------------------------------------------------------------#
class Doc_entradaViewSet(viewsets.ModelViewSet):
    queryset = Doc_entrada.objects.all()
    serializer_class = Doc_entradaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['num_nota']
    search_fields = ['num_nota', 'cod_forn']
#--------------------------------------------------------------------------------------#
