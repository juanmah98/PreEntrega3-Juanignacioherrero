from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class prodcutosFormulario(forms.Form):

    producto = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    color = forms.CharField() 

class contactoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    mensaje = forms.CharField()

class devolucionFormulario(forms.Form):
    numero_orden = forms.IntegerField()
    fecha_compra = forms.DateField()
    telefono = forms.IntegerField()
    nombre_apellido = forms.CharField()
    prendas_motivo = forms.CharField() 
    domicilio = forms.CharField()

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User 
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]