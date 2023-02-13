from django.urls import path
from App1.views import *

urlpatterns = [ 
    path('inicio/', inicio, name="INICIO"),
    path("producto/", producto, name="PRODUCTO"),
    path("contacto/", contacto, name="CONTACTO"),
    path("devolucion/", devolucion, name="DEVOLUCION"),
    
    #Creando Forms con django 
    path("Crear_productos/", Crear_productos, name= "Crear Prodcutos" ),
    path("Crear_contacto/", Crear_contacto, name= "Crear Contacto" ),
    path("Crear_devolucion/", Crear_devolucion, name= "Crear Devolucion" ),

    #Buscar info
    path("buscar_productos/", BuscarProductos , name="Buscar Prodcutos"),
    path("resultado_productos/", ResultadoProductos , name="Resultado Prodcutos")
]