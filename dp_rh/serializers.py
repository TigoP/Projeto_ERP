from rest_framework import serializers
from dp_rh.models import Departamento, Cargo

class DepartamentoSerializer(serializers.ModelSerializer):
    cod_dep = serializers.CharField(
        help_text="Deixe este campo em branco"
    )

    class Meta:
        model = Departamento
        fields = '__all__'
#--------------------------------------------------------------------------------------#
class CargoSerializer(serializers.ModelSerializer):
    cod_cargo = serializers.CharField(
        max_length=6, 
        required=False, 
        allow_blank=True, 
        help_text="Deixe este campo em branco"
    )

    class Meta:
        model = Cargo
        fields = '__all__'
#--------------------------------------------------------------------------------------#