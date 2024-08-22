from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque
from compras.serializers import FornecedorSerializer, ProdutoSerializer, Pedido_comprasSerializer, Item_pedido_comprasSerializer, EstoqueSerializer
from rest_framework import viewsets

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class Pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Pedido_compras.objects.all()
    serializer_class = Pedido_comprasSerializer

    def create_pedido(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

class Item_pedido_comprasViewSet(viewsets.ModelViewSet):
    queryset = Item_pedido_compras.objects.all()
    serializer_class = Item_pedido_comprasSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
