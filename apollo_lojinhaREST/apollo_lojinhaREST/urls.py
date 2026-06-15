from django.contrib import admin
from django.urls import path, include
from Contas.views import ContaPadraoViewSets
from Produtos.views import ProdutosViewSets, VariacaoProdutoViewSets
from Carrinho.views import CarrinhoViewSets, ItemCarrinhoViewSets, ListaCarrinhoPorContaViewSet, ListaItemPorCarrinhoViewSet
from suporte.views import SuporteViewSet
from Pedidos.views import PedidosViewsets
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação da API feita para o Trainee da EJECT",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()# rota, viewset, nome. são os que aparecem na API Root
router.register('auth/register', ContaPadraoViewSets, basename='Contas')
router.register('products', ProdutosViewSets, basename='Produtos')
router.register('variations', VariacaoProdutoViewSets, basename='Variação de produto')
router.register('cart', CarrinhoViewSets, basename='Carrinhos')
router.register('itemCarrinho', ItemCarrinhoViewSets, basename='Itens  no carrinho')
router.register('orders', PedidosViewsets, basename='Pedidos' )
router.register('suporte', SuporteViewSet, basename='Suporte')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('contas/<int:pkcontas>/carrinhos/', ListaCarrinhoPorContaViewSet.as_view()),
    path('contas/<int:pkcontas>/carrinhos/<int:pkcarrinhos>/', ListaItemPorCarrinhoViewSet.as_view()),
    
    path('auth/login/', TokenObtainPairView.as_view()), # token/        - ok
    path('auth/refresh/', TokenRefreshView.as_view()), # token/refresh  - ok
    #path('auth/forgot-password',EsqueciSenha.as_view()),
    #path('auth/forgot-password',RecuperarSenha.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
