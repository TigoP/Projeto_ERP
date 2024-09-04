from django.shortcuts import render
from rest_framework import viewsets
from dp_rh.models import Departamento, Cargo, Funcionario
from dp_rh.serializers import DepartamentoSerializer, CargoSerializer, FuncionarioSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
#--------------------------------------------------------------------------------------#
class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
#--------------------------------------------------------------------------------------#
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
#--------------------------------------------------------------------------------------#
