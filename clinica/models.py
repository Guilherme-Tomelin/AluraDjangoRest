from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    alergias = models.TextField()
    medicamentos_em_uso = models.TextField()

    def __str__(self):
        return self.nome
    
class Clinica(models.Model):

    ESPECIALIDADE = (
        ('1','Cardiologia'),
        ('2','Dermatologia'),
        ('3','Neurologia'),
        ('4','Psiquiatria'),
        ('5','Psicologia'),
        ('6','Odontologia'),
        ('7','Fisioterapia'),
        ('8','Pediatria')
        
    )

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=1, choices=ESPECIALIDADE, blank=False, null=False, default='1')
    pacientes = models.ManyToManyField('Paciente', related_name='clinicas_internacao')

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

