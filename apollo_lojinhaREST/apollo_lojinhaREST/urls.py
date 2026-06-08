from django.contrib import admin
from django.urls import path, include
from Contas.views import ContaPadraoViewSets
from Produtos.views import ProdutosViewSets, VariacaoProdutoViewSets
from Carrinho.views import CarrinhoViewSets, ItemCarrinhoViewSets, ListaCarrinhoPorContaViewSet, ListaItemPorCarrinhoViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()# rota, viewset, nome. são os que aparecem na API Root
router.register('auth/register', ContaPadraoViewSets, basename='Contas')
router.register('products', ProdutosViewSets, basename='Produtos')
router.register('variations', VariacaoProdutoViewSets, basename='Variação de produto')
router.register('cart', CarrinhoViewSets, basename='Carrinhos')
router.register('itemCarrinho', ItemCarrinhoViewSets, basename='Itens  no carrinho')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('contas/<int:pkcontas>/carrinhos', ListaCarrinhoPorContaViewSet.as_view()),
    path('contas/<int:pkcontas>/carrinhos/<int:pkcarrinhos>', ListaItemPorCarrinhoViewSet.as_view()),
    path('auth/login', TokenObtainPairView.as_view()), # token/        - ok
    path('auth/refresh', TokenRefreshView.as_view()), # token/refresh  - ok
    #path('auth/forgot-password',EsqueciSenha.as_view()),
    #path('auth/forgot-password',RecuperarSenha.as_view()),


]
