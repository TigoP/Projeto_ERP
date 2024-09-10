from dp_rh.serializers import DepartamentoSerializer, CargoSerializer, FuncionarioSerializer, Vencimento_salSerializer, Desconto_salSerializer
from dp_rh.models import Departamento, Cargo, Funcionario, Vencimento_sal, Desconto_sal
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.shortcuts import render

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nm_dep']
    search_fields = ['nm_dep']
#--------------------------------------------------------------------------------------#
class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nm_funcao']
    search_fields = ['nm_funcao', 'departamento']
#--------------------------------------------------------------------------------------#
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nm_funcionario']
    search_fields = ['nm_funcionario', 'cargo_func']
#--------------------------------------------------------------------------------------#
class Vencimento_salViewSet(viewsets.ModelViewSet):
    queryset = Vencimento_sal.objects.all()
    serializer_class = Vencimento_salSerializer
#--------------------------------------------------------------------------------------#
class Desconto_salViewSet(viewsets.ModelViewSet):
    queryset = Desconto_sal.objects.all()
    serializer_class = Desconto_salSerializer
#--------------------------------------------------------------------------------------#