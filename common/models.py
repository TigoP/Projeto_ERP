from django.db import models

class Endereco(models.Model):
    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
    )

    logradouro = models.TextField(max_length=120)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=2, choices=ESTADO,blank=False, default='')
    complemento = models.TextField(max_length=100)
    
    def __str__(self):
        return f'{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade} - {self.cep} - {self.estado} - {self.complemento}'
