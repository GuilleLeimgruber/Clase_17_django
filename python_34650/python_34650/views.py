
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render




def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def otra_vista_mas(request):
    return HttpResponse("Aca hay otra vista mas!!!") 

def fecha_de_hoy(request):
    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es {hoy}')

def vista_con_edad(request, edad):
    return HttpResponse(f'Mi edad es {edad}')

def mi_nombres_es(self, nombre):
    documento_texto = f"Mi nonbre es: <br> <br> {nombre}"    
    return HttpResponse(documento_texto)

def vista_con_template(request):
    return render(request, 'template_1.html', context = {})