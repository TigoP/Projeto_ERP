from compras.models import Fornecedor, Produto, Pedido_compras, Item_pedido_compras, Estoque, Doc_entrada
from compras.validators import cnpj_invalid, ie_invalid 
from common.serializers import EnderecoSerializer
from financeiro.models import Contas_pagar
from rest_framework import serializers
from common.models import Endereco
from django.db import transaction
from datetime import timedelta

class FornecedorSerializer(serializers.ModelSerializer):
    end_forn = EnderecoSerializer()  #import do endereço para mescla no fornecedor
    cod_forn = serializers.CharField(
        max_length=6, 
        required=False, 
        allow_blank=True, 
        help_text="Deixe este campo em branco"
    )

    class Meta:
        model = Fornecedor
        '''
            importe dos campos em listas para organizar a sequencia dos labels
        '''
        fields = ['cod_forn', 'nm_fantasia', 'rz_social', 'cnpj', 'ie', 'nm_contato', 'email', 'telefone', 'status', 'end_forn']         

    def validate(self, dados):
        '''
        Função que valida possiveis erros
        '''
        if cnpj_invalid(dados['cnpj']):
            raise serializers.ValidationError({'cnpj': 'O CNPJ deve conter 14 digitos!'})
        if ie_invalid(dados['ie']):
            raise serializers.ValidationError({'ie': 'A IE deve conter 11 digitos'})
        return dados
    
    def create(self, validated_data):
        '''
        Função que valida endereço já existe. Se sim, o exclui e habilita a criação. Se não, somente habilita a criação.
        '''
        endereco_data = validated_data.pop('end_forn', None)

        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
        else:
            endereco = None

        fornecedor = Fornecedor.objects.create(end_forn=endereco, **validated_data)
        return fornecedor
    
    def update(self, instance, validated_data):
        '''
        Função que extrai, atualiza e cria itens no pedido de compras
        '''
        endereco_data = validated_data.pop('end_forn', None)
        
        if endereco_data:
            if instance.end_forn: #verifica se ja tem endereço neste fornecedor
                for attr, value in endereco_data.items(): #Para cada atributo (attr) no endereco_data, ele usa setattr() para definir o novo valor (value) no objeto de endereço (instance.end_forn).
                    setattr(instance.end_forn, attr, value)
                instance.end_forn.save()
            else:
                endereco = Endereco.objects.create(**endereco_data) #Cria um novo endereço se não houver
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

#--------------------------------------------------------------------------------------#
class ProdutoSerializer(serializers.ModelSerializer):
    cod_prod = serializers.CharField(
        max_length=6, 
        required=False, 
        allow_blank=True, 
        help_text="Deixe este campo em branco"
    )
    class Meta:
        model = Produto
        fields = ['cod_prod', 'descricao', 'un_medida']
#--------------------------------------------------------------------------------------#
class Item_pedido_comprasSerializer(serializers.ModelSerializer):
    item_nm = serializers.SerializerMethodField() #permite personalizar o atributo

    class Meta:
        model = Item_pedido_compras
        fields = ['ped_compras', 'item', 'item_nm', 'qtd', 'preco_unitario', 'valor_total']

    def get_item_nm(self, obj):
        return f'{obj.item.id} - {obj.item.descricao}'
#--------------------------------------------------------------------------------------#
class Pedido_comprasSerializer(serializers.ModelSerializer):
    nome_forn = serializers.SerializerMethodField()
    pedido = serializers.CharField(
        max_length=6, 
        required=False, 
        allow_blank=True, 
        help_text="Deixe este campo em branco"
    )

    class Meta:
        model = Pedido_compras
        fields = ['pedido', 'emissao','fornecedor', 'nome_forn', 'status']
    
    def get_nome_forn(self, obj):
        return f'{obj.fornecedor.id} - {obj.fornecedor.rz_social}'
#--------------------------------------------------------------------------------------#
class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'
#--------------------------------------------------------------------------------------#
class Doc_entradaSerializer(serializers.ModelSerializer):

    item_nf_compra = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())
    valor_total = serializers.SerializerMethodField()

    class Meta:
        model = Doc_entrada
        fields = ['num_nota', 'serie_nt', 'dt_emissao', 'cod_forn', 'tipo_nf', 'cond_pgto', 'forma_pgto', 'vencimento', 'item_nf_compra', 'qtd_item', 'preco_unitario', 'valor_total']
    
    #def validate(self, dados):
    #    if num_nota_invalid(dados['num_nota']):
    #        raise serializers.ValidationError({'num_nota': 'O numero de NF deve conter 9 digitos!'})
    #    return dados

    def get_valor_total(self, obj):
        return obj.calcular_vlr_total()
    
    @transaction.atomic #garante que a transação sera atomica (utilizará tudo ou nada)
    def create(self, validated_data):
        '''
        Verifica se ha itens cadastrados, salva, extrai e apensa ao doc de entrada, possibilitando a criação de novo item
        '''
        doc_entrada = Doc_entrada.objects.create(**validated_data)

        try:
            '''
            verifica a classe Estoque, pega o produto.
            Adiciona o saldo de acordo com o inserido no doc entrada
            Se não houver item lá, cria e atualiza o saldo
            '''
            estoque = Estoque.objects.get(doc_entrada.item_nf_compra)
            estoque.adicionar_estoque(doc_entrada.qtd_item)
        except:
            Estoque.objects.create(produto=doc_entrada.item_nf_compra, saldo_est=doc_entrada.qtd_item)

        valor_total = doc_entrada.calcular_vlr_total()

        def criar_parcelas(doc_entrada, qtd_parcelas, intervalo_dias):
            valor_total = doc_entrada.calcular_vlr_total()
            valor_parcela = valor_total / qtd_parcelas

            for i in range(qtd_parcelas):
                vencimento = doc_entrada.dt_emissao + timedelta(days=(i + 1) * intervalo_dias)

                Contas_pagar.objects.create(
                documento = doc_entrada,
                descricao=f"Parcela {i + 1} - {doc_entrada.num_nota}",
                valor=valor_parcela,
                data_vencimento=vencimento,
                status='Pendente',
                fornecedor=doc_entrada.cod_forn
            )
        if doc_entrada.cond_pgto == '002':
            criar_parcelas(doc_entrada, qtd_parcelas=1, intervalo_dias=7)
        elif doc_entrada.cond_pgto == '003':
            criar_parcelas(doc_entrada, qtd_parcelas=1, intervalo_dias=30)
        elif doc_entrada.cond_pgto == '020':
            criar_parcelas(doc_entrada, qtd_parcelas=2, intervalo_dias=30)
        elif doc_entrada.cond_pgto == '021':
            criar_parcelas(doc_entrada, qtd_parcelas=3, intervalo_dias=30)
        else:
            criar_parcelas(doc_entrada, qtd_parcelas=0, intervalo_dias=0)

        return doc_entrada
#--------------------------------------------------------------------------------------#
