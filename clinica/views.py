from rest_framework import viewsets, generics
from clinica.models import Clinica, Paciente, Consulta
from clinica.serializer import ClinicaSerializer, PacienteSerializer, ConsultaSerializer, ListaConsultasPacienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PacientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos Pacientes"""
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ClinicasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Clinicas"""
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Consultas"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaConsultasPaciente(generics.ListAPIView):
    """Listando as Consultas de um Paciente"""
    def get_queryset(self):
        queryset = Consulta.objects.filter(paciente_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaConsultasPacienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]