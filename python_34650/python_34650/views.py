
from django.http import HttpResponse




def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def otra_vista_mas(request):
    return HttpResponse("Aca hay otra vista mas!!!") 
