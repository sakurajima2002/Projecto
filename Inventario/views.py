from django.shortcuts import redirect, render
from .models import Categoria , Producto
from .forms import *

# Create your views here.

def Inventario(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'Inventario/inventario.html',{'productos':productos,'categorias':categorias})

def Categorias(request , categoria_id):
    idcategoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=idcategoria)
    categorias = Categoria.objects.all()
    return render(request, 'Categorias/categorias.html',{'productos':productos , 'categorias':categorias})

def ListaCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'Categorias/listaCategorias.html',{'categorias':categorias})

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inventario')
    else:
        form = ProductoForm()
    return render(request, 'Inventario/agregarProducto.html',{'form':form})

def editarProducto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoEditForm(request.POST , instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Inventario')
    else:
        form = ProductoEditForm(instance=producto)
    return render(request, 'Inventario/editarProducto.html', {'form': form})

def eliminarProducto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('Inventario')

def agregarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaCategorias')
    else:
        form = CategoriaForm()
    return render(request, 'Categorias/agregarCategoria.html', {'form': form})

def editarCategoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST , instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('ListaCategorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'Categorias/editarCategoria.html', {'form': form})

def eliminarCategoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    categoria.delete()
    return redirect('ListaCategorias')
