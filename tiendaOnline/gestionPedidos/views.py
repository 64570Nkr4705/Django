from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

class Persona():
    def __init__(self, profesion, nombre, apellido):
        self.profesion = profesion
        self.nombre = nombre
        self.apellido = apellido
        
def Plantilla(request):
    
    p1 = Persona('Profesor', 'Gaston', 'Gomez')
    
    return render(request, 'template.html', {'profesionPersona':p1.profesion, 'nombrePersona':p1.nombre, 'apellidoPersona':p1.apellido})

def busquedaProductos(request):
    return render(request, "busquedaProductos.html")

def buscar(request):
    
    if request.GET['prd']:    
        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET['prd']
        
        
        if len(producto) > 20:
            mensaje='Texto de busqueda demasiado largo'
        
        else:
            
        
            '''filtrara el nombre que viaje en la variable producto
                y mostrara todo lo relacionando con esa palabra'''
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            
            return render(request, 'reultadosBusquedas.html', {"articulos":articulos, "query":producto})
            
    else:
        mensaje='No has introducido nada'
        
    return HttpResponse(mensaje)

def contacto(request):
        
    return render(request, 'contacto.html')