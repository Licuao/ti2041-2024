from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Caracteristica, Categoria, Marca
from django.contrib import messages
from .forms import ProductoForm, CaracteristicaFormSet

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('lista_productos')
        else:
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'productos/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
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
    return render(request, 'productos/crear_producto.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})
