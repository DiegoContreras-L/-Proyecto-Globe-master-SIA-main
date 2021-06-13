from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.IntegerField()
    rut=models.BigIntegerField()
    direccion=models.CharField(max_length=10)

class producto(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    fecha=models.DateField()
    cantidadActual=models.IntegerField()
    cantidadMinima=models.IntegerField()

class venta(models.Model):
    fecha=models.DateField()
    total=models.IntegerField()
    rutCliente=models.IntegerField()

class boleta(models.Model):
    codigo=models.IntegerField(primary_key=True)
    total=models.IntegerField()
    fecha=models.DateField()

class gasto(models.Model):
    codigo=models.IntegerField(primary_key=True)
    fecha=models.DateField()
    total=models.IntegerField()

class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.IntegerField()
    rut=models.BigIntegerField()
    direccion=models.CharField(max_length=50)





