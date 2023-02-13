from django import forms 

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