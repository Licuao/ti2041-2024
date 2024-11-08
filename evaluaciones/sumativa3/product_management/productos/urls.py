from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/id', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/id', views.eliminar_producto, name='eliminar_producto'),
]