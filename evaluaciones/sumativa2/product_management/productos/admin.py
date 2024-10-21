from django.contrib import admin
from .models import Categoria, Marca, Producto, Caracteristica

admin.site.register(Categoria)
admin.site.register(Marca)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'categoria', 'marca')
    search_fields = ('codigo', 'nombre')
    list_filter = ('categoria', 'marca')

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'nombre', 'valor')
    list_filter = ('nombre',)