from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Caracteristica(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='caracteristicas')
    nombre = models.CharField(max_length=100, default='Característica')
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"