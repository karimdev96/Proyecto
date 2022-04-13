"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App import views
urlpatterns = [
    path('', views.inicio, name='inicio'),#listo
    path('familia', views.familia, name='familia'),#listo
    path('trabajo', views.trabajo, name='trabajo'),#listo
    path('profesion', views.master, name='profesion'),#listo

    path('buscar', views.busqueda, name='search'),#listo
    path('result', views.search, name="result"),#listo

    path('delete/<name2>/', views.borrar, name='del'),#listo
    path('delete2/<name4>/', views.borrar2, name='del2'),#listo
    path('delete3/<name5>/', views.borrar3, name='del3'),#listo

    path('edit/<name3>/', views.editarProfesor, name='edit2'),#listo
    path('edit/<name3>/', views.editarProfesor, name='edit3'),#listo
    path('edit/<name3>/', views.editarProfesor, name='edit4'),#todavia no
]