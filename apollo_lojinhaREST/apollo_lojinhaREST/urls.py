from django.contrib import admin
from django.urls import path, include
from Contas.views import ContaPadraoViewSets
from Produtos.views import ProdutosViewSets, VariacaoProdutoViewSets
from Carrinho.views import CarrinhoViewSets, ItemCarrinhoViewSets, ListaCarrinhoPorContaViewSet, ListaItemPorCarrinhoViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()# rota, viewset, nome. são os que aparecem na API Root
router.register('contas', ContaPadraoViewSets, basename='Contas')
router.register('produtos', ProdutosViewSets, basename='Produtos')
router.register('variacao', VariacaoProdutoViewSets, basename='Variação de produto')
router.register('carrinho', CarrinhoViewSets, basename='Carrinhos')
router.register('itemCarrinho', ItemCarrinhoViewSets, basename='ItensCarrinho')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('contas/<int:pkcontas>/carrinhos', ListaCarrinhoPorContaViewSet.as_view()),
    path('contas/<int:pkcontas>/carrinhos/<int:pkcarrinhos>', ListaItemPorCarrinhoViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),

]
