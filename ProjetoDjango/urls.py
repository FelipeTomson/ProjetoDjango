from django.contrib import admin
from django.urls import path
from AppCadUsuarios import views


urlpatterns = [
    # rota, view responsável, nome de referencia
    # usuarios.com
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagemUsuarios')

]
