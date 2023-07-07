from rest_framework import serializers
from clinica.models import Paciente, Clinica, Consulta


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ListaConsultasPacienteSerializer(serializers.ModelSerializer):
    
    clinica = serializers.ReadOnlyField(source = 'clinica.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Consulta
        fields = ['clinica','periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()