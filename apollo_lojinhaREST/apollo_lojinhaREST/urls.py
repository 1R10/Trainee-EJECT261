from django.contrib import admin
from django.urls import path, include
from Contas.views import ContaPadraoViewSets
from Produtos.views import ProdutosViewSets
from Carrinho.views import CarrinhoViewSets
from rest_framework import routers

router = routers.DefaultRouter()# rota, viewset, nome
router.register('contas', ContaPadraoViewSets, basename='ContaPadrao')
router.register('produtos', ProdutosViewSets, basename='Produtos')
router.register('carrinho', CarrinhoViewSets, basename='Carrinhos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
