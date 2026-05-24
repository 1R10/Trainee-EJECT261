from django.contrib import admin

from Produtos.models import Produtos

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nomeProduto', 
                    'descricaoProduto',
                    'precoProduto',
                    'tamanhoProduto',
                    'corProduto',
                    'estoqueProduto' )
    
    list_display_links = ('nomeProduto',)
    list_per_page      = 20
    search_fields      = ('nomeProduto','corProduto')

admin.site.register(Produtos,ProdutoAdmin)