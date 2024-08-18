from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque
from compras.serializers import FornecedorSerializer, ProdutoSerializer, Pedido_comprasSerializer, Item_pedido_comprasSerializer, EstoqueSerializer
from rest_framework import viewsets

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer = FornecedorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer = ProdutoSerializer

class Pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Pedido_compras.objects.all()
    serializer = Pedido_comprasSerializer

class Item_pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Item_pedido_compras.objects.all()
    serializer = Item_pedido_comprasSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer = EstoqueSerializer
