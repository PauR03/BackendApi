from django.http import JsonResponse
from .models import *

# from rest_framework.decorators import api_view

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

def añadirProducto(request):

    # producto = Producto.objects.create(
    #     nombre = request.POST.get('nombre'),
    #     descripcion = request.POST.get('descripcion'),
    #     precio = request.POST.get('precio')
    # )
    print("\n"*20)
    print(request.POST.get('nombre'))
    return JsonResponse({
        "status": "OK",
        "producto": "request"
    })