from django.contrib import admin
from clinica.models import Paciente, Clinica, Consulta
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models



class Pacientes(admin.ModelAdmin):
    list_display = ('id','nome','data_nascimento','genero','altura','peso','alergias','medicamentos_em_uso')
    list_display_links = ('id', 'nome')
    search_fields = ('id','nome',)
    list_per_page = 20

admin.site.register(Paciente, Pacientes)


class PacientesInline(admin.TabularInline):
    model = Clinica.pacientes.through
    extra = 1
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(verbose_name='Pacientes', is_stacked=False)},
    }

class Clinicas(admin.ModelAdmin):
    list_display = ('id','nome','endereco','telefone','especialidade')
    list_display_links = ('id', 'nome')
    search_fields = ('id','nome',)
    inlines = [PacientesInline]
    list_per_page = 20

admin.site.register(Clinica, Clinicas)



class Consultas(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'clinica', 'periodo')
    list_display_links = ('id',)

admin.site.register(Consulta, Consultas)
