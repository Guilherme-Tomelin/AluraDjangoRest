from django.contrib import admin
from django.urls import path, include
from clinica.views import PacientesViewSet, ClinicasViewSet, ConsultasViewSet, ListaConsultasPaciente
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pacientes', PacientesViewSet, basename='Pacientes')
router.register('clinicas', ClinicasViewSet, basename='Clinicas')
router.register('consultas', ConsultasViewSet, basename='Consultas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('paciente/<int:pk>/consultas', ListaConsultasPaciente.as_view())
]
