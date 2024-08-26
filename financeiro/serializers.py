from rest_framework import serializers
from financeiro.models import Conta_bancaria, Contas_pagar, Contas_receber, Mov_bancario

class Conta_bancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta_bancaria
        fields = '__all__'
#--------------------------------------------------------------------------------------#
class Contas_pagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas_pagar
        fields = '__all__'
#--------------------------------------------------------------------------------------#
class Contas_receberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas_receber
        fields = '__all__'
#--------------------------------------------------------------------------------------#
class Mov_bancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mov_bancario
        fields = '__all__'
#--------------------------------------------------------------------------------------#
