from django.urls import path
from . import views

urlpatterns = [
     path('productosAdmin/', views.productosAdmin, name='productosAdmin'),
    path('productosUsuario/', views.productosUsuario, name='productosUsuario'),
    path('crearProducto/', views.crearProducto, name='crearProducto'),
    path('editarProducto/<int:id>/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    path('listaCategoria/', views.listaCategoria, name='listaCategoria'),
    path('crearCategoria/', views.crearCategoria, name='crearCategoria'),
    path('editarCategoria/<int:id>/', views.editarCategoria, name='editarCategoria'),
    path('eliminarCategoria/<int:id>/', views.eliminarCategoria, name='eliminarCategoria'),
]