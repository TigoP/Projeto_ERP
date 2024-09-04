from rest_framework import serializers
from dp_rh.models import Departamento, Cargo, Funcionario
from common.models import Endereco
from common.serializers import EnderecoSerializer

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
class FuncionarioSerializer(serializers.ModelSerializer):
    end_func = EnderecoSerializer()

    cod_funci = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text='Deixe este campo em branco'
    )

    class Meta:
        model = Funcionario
        fields = ('cod_funci', 'nm_funcionario', 'cpf', 'rg', 'dt_nasc', 'nacionalidade', 'estado_civil', 'sexo', 'cargo_func', 'salario', 'dt_admissao', 'depart_func', 'situacao', 'end_func')

    def create(self, validated_data):
        '''
        Função que valida se o endereço já existe. Se sim, o exclui e habilita a criação. Se não, somente habilita a criação.
        '''
        endereco_data = validated_data.pop('end_func', None)

        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
        else:
            endereco = None

        funcionario = Funcionario.objects.create(end_func=endereco, **validated_data)
        
        return funcionario
