from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    #list_display: sirve para que aparezcan los campos especificados por pantalla
    list_display=('nombre', 'direccion', 'phone')
    #search_fields: sirve para agregar un buscardor con los argumentos especificados
    search_fields=('nombre', 'phone')

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion', )
    search_fields=('nombre', 'precio')
    
class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha')
    list_filter=('fecha', )
    date_hierarchy='fecha'

admin.site.register(Clientes, ClienteAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)