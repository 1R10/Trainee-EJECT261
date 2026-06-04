from django.contrib import admin
from Carrinho.models import Carrinho, ItemCarrinho

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('dono',
                    'estado',
                    'carrinhoData',)
    
    list_display_links = ('dono', 'carrinhoData')
    list_per_page      = 10
    search_fields      = ('dono', 'carrinhoData')
    ordering           = ('carrinhoData',)

admin.site.register(Carrinho,CarrinhoAdmin)

class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho',
                    'produto',
                    'quantidade',)
    
    list_display_links = ('carrinho', 'produto')
    list_per_page      = 30
    search_fields      = ('carrinho', 'produto')
    ordering           = ('carrinho',)

admin.site.register(ItemCarrinho,ItemCarrinhoAdmin)