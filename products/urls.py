from django.urls import path, include
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register('productsList', ProductosListViewSet,"productsList")
router.register('products', ProductoViewSet,"products")
#router.register('categorias', CategoriasViewSet,"categorias")
router.register('grosor', GrosorViewSet,"grosor")
router.register('color', ColorViewSet,"color")
router.register('accesorios', AccesoriosViewSet,"accesorios")
#router.register('categoriasList',CategoriasListViewSet,"categoriasList")

urlpatterns = [
    path('',include(router.urls)),
]

