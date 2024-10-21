from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Producto, Caracteristica, Categoria, Marca
from .forms import ProductoForm, CaracteristicaFormSet

def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    categoria_id = request.GET.get('categoria')
    marca_id = request.GET.get('marca')

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if marca_id:
        productos = productos.filter(marca_id=marca_id)

    context = {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
    }
    return render(request, 'productos/lista_productos.html', context)

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            caracteristica_formset = CaracteristicaFormSet(request.POST, instance=producto)
            if caracteristica_formset.is_valid():
                caracteristica_formset.save()
            return redirect('resultado_creacion', producto_id=producto.id)
    else:
        form = ProductoForm()
        caracteristica_formset = CaracteristicaFormSet()
    
    return render(request, 'productos/crear_producto.html', {
        'form': form,
        'caracteristica_formset': caracteristica_formset,
    })

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            caracteristica_formset = CaracteristicaFormSet(request.POST, instance=producto)
            if caracteristica_formset.is_valid():
                caracteristica_formset.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
        caracteristica_formset = CaracteristicaFormSet(instance=producto)
    
    return render(request, 'productos/editar_producto.html', {
        'form': form,
        'caracteristica_formset': caracteristica_formset,
        'producto': producto,
    })

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def resultado_creacion(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/resultado_creacion.html', {'producto': producto})