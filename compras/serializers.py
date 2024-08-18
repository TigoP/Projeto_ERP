from rest_framework import serializers
from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        exclude = []

class Pedido_comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_compras
        fields = '__all__'

class Item_pedido_comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_pedido_compras
        exclude = []

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'
