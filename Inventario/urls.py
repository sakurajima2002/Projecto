from django.urls import path
from Inventario import views

urlpatterns = [
    path('',views.Inventario,name='Inventario'),
    path('listaCategorias/',views.ListaCategorias,name='ListaCategorias'),
    path('categoria/<int:categoria_id>/',views.Categorias,name='Categorias'),
    path('agregarProducto/',views.agregarProducto,name='AgregarProducto'),
    path('editarProducto/<int:producto_id>/',views.editarProducto,name='EditarProducto'),
    path('eliminarProducto/<int:producto_id>/',views.eliminarProducto,name='EliminarProducto'),
    path('agregarCategoria/',views.agregarCategoria,name='AgregarCategoria'),
    path('eliminarCategoria/<int:categoria_id>/',views.eliminarCategoria,name='EliminarCategoria'),
    path('editarCategoria/<int:categoria_id>/',views.editarCategoria,name='EditarCategoria'),
]