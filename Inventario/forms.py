from django import forms
from .models import Producto , Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'precio_producto',
            'cantidad_producto',
            'categoria'
        ]

class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'precio_producto',
            'cantidad_producto',
            'categoria'
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
