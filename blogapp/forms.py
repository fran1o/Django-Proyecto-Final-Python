from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MascotaFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    animal = forms.CharField(max_length=200)
    raza = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=100)
    color = forms.CharField(max_length=200)
    imagen = forms.ImageField()

class UsuarioRegisterFormulario(UserCreationForm):

    #Datos de Usario
    username = forms.CharField(label="username")
    nombre = forms.CharField(label="nombre")
    apellido = forms.CharField(label="apellido")
    email = forms.EmailField(label="email")
    celular = forms.IntegerField(label="celular")

    class Meta:
        model = User
        fields = ["username", "nombre", "apellido", "email", "celular"]


class ContactoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    asunto = forms.CharField(max_length=50)
    mensaje = forms.CharField()


class AdoptarFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    celular = forms.IntegerField()
    direccion = forms.CharField(max_length=200)

class AvatarForm(forms.Form):


    model = User
    img = forms.ImageField(label="Ingrese una foto")
