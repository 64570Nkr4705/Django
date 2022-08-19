from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    
    formContacto=FormularioContacto(data=request.POST)
    if formContacto.is_valid():
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        contenido=request.POST.get('contenido')
        
        email=EmailMessage("Mensaje desde App Django",
        "El ususrio con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre,email,contenido),
        "", ["gomezgastonkr4705@gmail.com"], reply_to=[email])
        try:
            email.send()
        
            return redirect('/contacto/?valido')
        except:
            return redirect('/contacto/?noValido')            
    
    return render(request, 'contacto/contacto.html', {'miFormulario':formContacto})