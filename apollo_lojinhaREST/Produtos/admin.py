from django.contrib import admin

from Produtos.models import Produtos, VariacaoProduto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
                    'nomeProduto', 
                    'descricaoProduto',
                    'precoProduto',
                    )
    
    list_display_links = ('nomeProduto',)
    list_per_page      = 20
    search_fields      = ('nomeProduto',)

admin.site.register(Produtos,ProdutoAdmin)

class VariacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto',
                    'tamanhoProduto',
                    'corProduto',
                    'estoqueProduto',
                    )
    list_display_links = ('produto', 'tamanhoProduto', 'corProduto')
    list_per_page      = 20
    search_fields      = ('tamanhoProduto', 'corProduto',)
admin.site.register(VariacaoProduto,VariacaoProdutoAdmin)
