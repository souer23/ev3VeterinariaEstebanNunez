from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

""" Evitar la reinserción de datos al recargar la página """
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden



# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"

def listaUsuarios(request):
    usuarios = User.objects.all()  # Obtiene todos los usuarios
    return render(request, 'gestorUser/indexAdmin.html', {'usuarios': usuarios})

def eliminarUsuario(request,id):
    #Buscar el usuario dentro de la base de datos con su id
    usuario = User.objects.get(id=id)
    if usuario.is_superuser:
        return HttpResponseForbidden("No puedes eliminar a un administrador.")
    usuario.delete()
    return HttpResponseRedirect(reverse('lista'))



