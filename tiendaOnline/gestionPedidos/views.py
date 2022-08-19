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
    if request.method == 'POST':
        miForm = FormularioContacto(request.POST)
        
        if miForm.is_valid():
            infoForm = miForm.cleaned_data
            
            send_mail(infoForm['asunto'], infoForm['mensaje'],
            infoForm.get('email', ' '), ['toongas777@gmail.com'],)
            
            return render(request, 'gracias.html')
    
    else:
        miForm = FormularioContacto()
        
    return render(request, 'formulario_contacto.html', {'form':miForm})

'''def contacto(request):
    
    if request.method == 'POST':
        subject = request.POST['asunto']
        
        message = request.POST['mensaje'] + ' ' + request.POST['email']
        
        email_from = settings.EMAIL_HOST_USER
        
        send_mail(subject, message, email_from, recipient_list)
        
        return render(request, 'gracias.html')
        
    return render(request, 'contacto.html')'''