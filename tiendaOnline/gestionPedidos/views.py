from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.

class Persona():
    def __init__(self, profesion, nombre, apellido):
        self.profesion = profesion
        self.nombre = nombre
        self.apellido = apellido
        
def Plantilla(request):
    
    p1 = Persona('Profesor', 'Gaston', 'Gomez')
    
    return render(request, 'template.html', {'profesionPersona':p1.profesion, 'nombrePersona':p1.nombre, 'apellidoPersona':p1.apellido})