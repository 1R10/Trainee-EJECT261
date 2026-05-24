from django.contrib import admin
from django.urls import path, include
from Contas.views import ContaPadraoViewSets
from Produtos.views import ProdutosViewSets
from Carrinho.views import CarrinhoViewSets, ItemCarrinhoViewSets, ListaCarrinhoPorContaViewSet, ListaItemPorCarrinhoViewSet
from rest_framework import routers

router = routers.DefaultRouter()# rota, viewset, nome
router.register('contas', ContaPadraoViewSets, basename='ContaPadrao')
router.register('produtos', ProdutosViewSets, basename='Produtos')
router.register('carrinho', CarrinhoViewSets, basename='Carrinhos')
router.register('itemCarrinho', ItemCarrinhoViewSets, basename='ItensCarrinho')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('contas/<int:pkcontas>/carrinhos', ListaCarrinhoPorContaViewSet.as_view()),
        path('contas/<int:pkcontas>/carrinhos/<int:pkcarrinhos>', ListaItemPorCarrinhoViewSet.as_view()),

]
