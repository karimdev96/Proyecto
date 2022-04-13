from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    FechaDeNacimiento = models.DateField()
    dni = models.IntegerField()
    edad= models.IntegerField()
    def __str__(self):
        return f'Nombre {self.nombre} - Apellido {self.apellido} - Fecha de Nacimiento {self.FechaDeNacimiento} - dni {self.dni} - parentezco {self.edad}'
class Trabajos(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    apellido_empresa = models.CharField(max_length=50)
    email_empresa = models.EmailField()
    dni_empresa = models.IntegerField()
    telefono_empresa = models.IntegerField()
    profesion_empresa = models.CharField(max_length=25)
    def __str__(self):
        return f'Nombre {self.nombre_empresa} - Apellido {self.apellido_empresa} - Email {self.email_empresa} - dni {self.dni_empresa} - Telefono {self.telefono_empresa} - Profesion {self.profesion_empresa}'


class Profesor(models.Model):
    nombre_master = models.CharField(max_length=50)
    apellido_master = models.CharField(max_length=50)
    email_master = models.EmailField()
    dni_master = models.IntegerField()
    telefono_master = models.IntegerField()
    profesion_master = models.CharField(max_length=25)
    def __str__(self):
        return f"Nombre {self.nombre_master} - Apellido {self.apellido_master} - Email {self.email_master} - dni {self.dni_master} - Telefono {self.telefono_master} - Profesion {self.profesion_master}"


