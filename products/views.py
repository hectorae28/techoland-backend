from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
from .serializers import ProductosListSerializer

""" @api_view(['GET'])
def categorias(request):
  categorias = Categoria.objects.all()
  serializer = ProductosListSerializer(categorias, many=True)
  return Response(serializer.data) """

@api_view(['GET'])
def product_list(request):
    """
    List all code productos, or create a new producto.
    """
    return JsonResponse({'categorias':Producto.objects.all()})
    """ 
    if request.method == 'GET':
        products = Producto.objects.all()
        serializer = ProductosListSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_RE QUEST)"""