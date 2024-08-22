from rest_framework import serializers
from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque
from common.serializers import EnderecoSerializer
from common.models import Endereco

class FornecedorSerializer(serializers.ModelSerializer):
    end_forn = EnderecoSerializer()  #import do endereço para mescla no fornecedor

    class Meta:
        model = Fornecedor
        '''
            importe dos campos em listas para organizar a sequencia dos labels
        '''
        fields = ['cod_forn', 'nm_fantasia', 'rz_social', 'cnpj', 'ie', 'nm_contato', 'email', 'telefone', 'status', 'end_forn']         

    '''
        Função que valida endereço já existe. Se sim, o exclui e habilita a criação. Se não, somente habilita a criação
    '''
    def create(self, validated_data):
        endereco_data = validated_data.pop('end_forn', None)

        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
        else:
            endereco = None

        fornecedor = Fornecedor.objects.create(end_forn=endereco, **validated_data)
        return fornecedor  

    '''
        Função que estrai, atualiza e cria itens no pedido de compras
    '''
    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('end_forn', None)
        
        if endereco_data:
            if instance.end_forn:
                for attr, value in endereco_data.items():
                    setattr(instance.end_forn, attr, value)
                instance.end_forn.save()
            else:
                endereco = Endereco.objects.create(**endereco_data)
                instance.end_forn = endereco

        instance.nm_fantasia = validated_data.get('nm_fantasia', instance.nm_fantasia)
        instance.rz_social = validated_data.get('rz_social', instance.rz_social)
        instance.nm_contato = validated_data.get('nm_contato', instance.nm_contato)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.ie = validated_data.get('ie', instance.ie)
        instance.nm_contato = validated_data.get('cnpj', instance.nm_contato)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.status = validated_data.get('cnpj', instance.status)
        instance.save()  

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class Item_pedido_comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_pedido_compras
        fields = ['ped_compras', 'item', 'qtd', 'preco_unitario', 'valor_total']

class Pedido_comprasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido_compras
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'
