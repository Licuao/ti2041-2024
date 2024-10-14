from django.db import models

  
class Categoria(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100, blank=False, null=False)

  def __str__(self):
    return self.nombre

class Marca(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)

  def __str__(self):
    return self.nombre

class Producto(models.Model):
  tamaño = (
    ('P', 'Pequeño'),
    ('M', 'Mediano'),
    ('G', 'Grande' )
  )
  codigo = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  tamaño = models.CharField(max_length=1,choices=tamaño, blank=False, null=False)
  peso = models.DecimalField(max_digits=10, decimal_places=2)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
  marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre