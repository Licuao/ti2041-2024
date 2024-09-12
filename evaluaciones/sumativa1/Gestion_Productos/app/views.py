from django.shortcuts import render, redirect

productos_registrados = []

def registro(request):
    if request.method == 'POST':

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        if codigo and nombre and marca and fecha_vencimiento:
            producto = {
                'codigo': codigo,
                'nombre': nombre,
                'marca': marca,
                'fecha_vencimiento': fecha_vencimiento,
            }
            productos_registrados.append(producto)
            return redirect('resultado')

    return render(request, 'productos/registro.html')

def resultado(request):
    return render(request, 'productos/resultado.html', {'productos': productos_registrados[-1]})

def consulta(request):
    return render(request, 'productos/consulta.html', {'productos': productos_registrados})
