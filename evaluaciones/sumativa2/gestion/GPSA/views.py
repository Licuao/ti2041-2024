
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})

def lista_productos(request):
    productos = Producto.objects.all()

    marca = request.GET.get('marca')
    categoria = request.GET.get('categoria')
    caracteristica = request.GET.get('caracteristica')

    if marca:
        productos = productos.filter(marca__icontains=marca)
    if categoria:
        productos = productos.filter(categoria__nombre__icontains=categoria)
    if caracteristica:
        productos = productos.filter(caracteristicas__nombre__icontains=caracteristica)

    return render(request, 'productos/lista.html', {'productos': productos})
