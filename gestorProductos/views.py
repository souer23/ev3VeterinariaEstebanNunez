from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Categoria
from .forms import CategoriaForm
from django.http import HttpResponseForbidden

def esAdmin(user):
    return user.is_superuser

@user_passes_test(esAdmin)
def listaCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/categoriasAdmin.html', {'categorias': categorias})




@user_passes_test(esAdmin)
def crearCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaCategoria')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/crearCategoria.html', {'form': form})

@user_passes_test(esAdmin)
def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listaCategoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/editarCategoria.html', {'form': form})

@user_passes_test(esAdmin)
def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('listaCategoria')

# Vista para el administrador
def productosAdmin(request):
    productos = Producto.objects.all()
    return render(request, 'gestorProductos/productosAdmin.html', {'productos': productos})

# Vista para el usuario
def productosUsuario(request):
    productos = Producto.objects.filter(creador=request.user)
    return render(request, 'gestorProductos/productosUser.html', {'productos': productos})

# Crear un producto
def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creador = request.user
            producto.save()
            return redirect('productosAdmin' if request.user.is_superuser else 'productosUsuario')  # Cambiar según la vista que desees redirigir
    else:
        form = ProductoForm()
    return render(request, 'gestorProductos/crearProducto.html', {'form': form})

# Editar un producto
def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)

    # Verificar que el usuario sea administrador o creador del producto
    if not (request.user.is_superuser or producto.creador == request.user):
        return HttpResponseForbidden("No tienes permisos para editar este producto.")
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productosAdmin' if request.user.is_superuser else 'productosUsuario')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'gestorProductos/editarProducto.html', {'form': form})


# Eliminar un producto
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.user == producto.creador or request.user.is_superuser:
        producto.delete()
    return redirect('productosAdmin' if request.user.is_superuser else 'productosUsuario')

