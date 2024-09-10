from financeiro.serializers import Conta_bancariaSerializer, Contas_pagarSerializer, Contas_receberSerializer, Mov_bancarioSerializer
from financeiro.models import Conta_bancaria, Contas_pagar, Contas_receber, Mov_bancario
from django.shortcuts import render
from rest_framework import viewsets

class Conta_bancariaViewSet(viewsets.ModelViewSet):
    queryset = Conta_bancaria.objects.all()
    serializer_class = Conta_bancariaSerializer
#--------------------------------------------------------------------------------------#
class Contas_pagarViewSet(viewsets.ModelViewSet):
    queryset = Contas_pagar.objects.all()
    serializer_class = Contas_pagarSerializer
#--------------------------------------------------------------------------------------#
class Contas_receberViewSet(viewsets.ModelViewSet):
    queryset = Contas_receber.objects.all()
    serializer_class = Contas_receberSerializer
#--------------------------------------------------------------------------------------#
class Mov_bancarioViewSet(viewsets.ModelViewSet):
    queryset = Mov_bancario.objects.all()
    serializer_class = Mov_bancarioSerializer
#--------------------------------------------------------------------------------------#
