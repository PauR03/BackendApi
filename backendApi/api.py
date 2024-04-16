from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view
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

@api_view(['POST'])
def añadirProducto(request):
    try:
        producto = Producto.objects.create(
            nombre = request.data.get('nombre'),
            descripcion = request.data.get('descripcion'),
            precio = request.data.get('precio')
        )
        return JsonResponse({
            "status": True
        })
    except:
        return JsonResponse({
            "status": False
        })

@api_view(['POST'])
def borrarProducto(request):
    try:
        producto = Producto.objects.get(id=request.data.get('id'))
        producto.delete()
        return JsonResponse({
            "status": True
        })
    except:
        return JsonResponse({
            "status": False
        })