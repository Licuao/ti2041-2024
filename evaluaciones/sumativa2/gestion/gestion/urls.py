from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from GPSA import views

urlpatterns = [
  path('', lambda request: redirect('lista_productos/')),
    path('admin/', admin.site.urls),
    path('crear/', views.crear_producto, name='lista_productos'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
