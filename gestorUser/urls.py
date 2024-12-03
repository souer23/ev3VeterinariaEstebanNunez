from django.urls import path

from gestorUser.views import SignUpView, listaUsuarios, eliminarUsuario

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('listaUsuarios/', listaUsuarios, name='lista'),
    path('eliminarUsuario/<int:id>', eliminarUsuario, name='eliminarUsuario'),
    ]