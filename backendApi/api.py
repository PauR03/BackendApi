from django.http import JsonResponse
from .models import *

def hello(request):
    # jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

def mostrarLista(request):
    productos = Producto.objects.values('id', 'nombre')
    return JsonResponse({
        "data": list(productos)
    })