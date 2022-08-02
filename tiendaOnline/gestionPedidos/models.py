from django.db import models

# Create your models here.

#Por cada cambio que se hace en el modelo se debe hacer una migracion
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50, verbose_name='La direccion')
    #los atributos blank y null, sirven para que el campo email sea opcional 
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Articulos(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()
    
    #Linea que sirve para el mensaje del bash de python(Articulos.objects.filter(atributo, valor))
    #para listar mayor o menor desde el shell se utiliza Ex: precio__gte=valor o precio __lte=valor
    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)
    
class Pedidos(models.Model):
    numero=models.IntegerField()
    #Si el campo fecha es .date funciona para filtros
    fecha=models.DateField()
    entregado=models.BooleanField()