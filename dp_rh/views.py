from dp_rh.serializers import DepartamentoSerializer, CargoSerializer, FuncionarioSerializer, Vencimento_salSerializer, Desconto_salSerializer
from dp_rh.models import Departamento, Cargo, Funcionario, Vencimento_sal, Desconto_sal
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.shortcuts import render

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nm_dep']
#--------------------------------------------------------------------------------------#
class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nm_funcao']
#--------------------------------------------------------------------------------------#
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nm_funcionario']
#--------------------------------------------------------------------------------------#
class Vencimento_salViewSet(viewsets.ModelViewSet):
    queryset = Vencimento_sal.objects.all()
    serializer_class = Vencimento_salSerializer
#--------------------------------------------------------------------------------------#
class Desconto_salViewSet(viewsets.ModelViewSet):
    queryset = Desconto_sal.objects.all()
    serializer_class = Desconto_salSerializer
#--------------------------------------------------------------------------------------#