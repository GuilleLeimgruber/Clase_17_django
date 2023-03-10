"""python_34650 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from python_34650.views import hola_mundo, otra_vista_mas, fecha_de_hoy, vista_con_edad,mi_nombres_es, vista_con_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo),
    path('otra_vista/', otra_vista_mas),
    path('fecha/', fecha_de_hoy),
    path('edad/<int:edad>/', vista_con_edad),
    path('nombre/<str:nombre>', mi_nombres_es),
    path('vista_template/', vista_con_template)
]
