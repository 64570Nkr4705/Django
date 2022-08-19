from django.shortcuts import render
from tienda.models import Producto, CategoriaProd

# Create your views here.

def tienda(request):
    
    productos=Producto.objects.all()
    
    return render(request, 'tienda/tienda.html', {'productos':productos})

'''def CategoriaProd(request, categoriaProd_id):
    
    categoria=CategoriaProd.objects.get(id=categoria_id)
    productos=Producots.objects.filter(categorias=categoria)
    
    return(request, 'tienda/tienda.html', {'categoria':categoria}, {'productos':productos})'''