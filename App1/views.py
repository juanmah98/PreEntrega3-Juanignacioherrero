from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate



def InicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra )

            if user:

                login(request, user)
                
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

                return render(request, "App1/inicio.html", {"mensaje":"DATOS INCORRECTOS."})
       
    else:

        form = AuthenticationForm()

    return render(request, "App1/login.html", {"formulario":form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "App1/inicio.html", {"mensaje":"Usuario Creado Con Exito!"})
        
    else:

        form = UsuarioRegistro()    

    return render(request, "App1/registro.html", {"formulario":form})




def inicio(request):
    return render(request, "App1/inicio.html") 

def producto(request):

    return render(request, "App1/producto.html")

def contacto(request):

    return render(request, "App1/contacto.html")

def devolucion(request):

    return render(request, "App1/devolucion.html")

def Crear_productos(request):
    
    if request.method == 'POST':

        miFormulario = productosFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            prodcuto1 = producto(nombre = infoDict["nombre"], tipo = infoDict["tipo"], talle = infoDict["talle"], color = infoDict["color"])

            prodcuto1.save()

            return render(request,"App1/inicio.html")
        
    else:

        miFormulario = productosFormulario()

    return render(request, "App1/CrearProducto.html", {"formulario1":miFormulario})

def Crear_contacto(request):
    
    if request.method == 'POST':

        miFormulario = contactoFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            contacto1 = contacto(nombre = infoDict["nombre"], apellido = infoDict["apellido"], email = infoDict["email"], telefono = infoDict["telefono"], mensaje = infoDict["mensaje"])

            contacto1.save()

            return render(request,"App1/inicio.html")
        
    else:

        miFormulario = contactoFormulario()

    return render(request, "App1/CrearContacto.html", {"formulario1":miFormulario})

def Crear_devolucion(request):
    
    if request.method == 'POST':

        miFormulario = devolucionFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            devolucion1 = producto(numero_orden = infoDict["numero_orden"], fecha_compra = infoDict["fecha_compra"], telefono = infoDict["telefono"], nombre_apellido = infoDict["nombre_apellido"],
                                  prenda_motivo = infoDict["prenda_motivo"], domicilio = infoDict["domicilio"])

            devolucion1.save()

            return render(request,"App1/inicio.html")
        
    else:

        miFormulario = devolucionFormulario()

    return render(request, "App1/CrearDevolucion.html", {"formulario1":miFormulario})

def BuscarProductos(request):

    return render(request, "App1/BusquedaProducto.html")

def ResultadoProductos(request):

    if request.method == "GET":
       
        productoBusqueda = request.GET["producto"]
       
        productoResultado = prodcutos.objects.filter(nombre__icontains=productoBusqueda)

        return render(request, "App1/ResultadoProducto.html", {"nombre":productoBusqueda, "resultado":productoResultado})
  
    return render(request, "App1/ResultadoProductos.html")