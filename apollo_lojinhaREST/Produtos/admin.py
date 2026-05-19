from django.contrib import admin

from Produtos.models import Produtos

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nomeProduto', 
                    'descricaoProduto',
                    'precoProduto',
                    'tamanhoProduto',
                    'corProduto' )
    
    list_display_links = ('nomeProduto',)
    list_per_page      = 20
    search_fields      = ('nomeProduto',)

admin.site.register(Produtos,ProdutoAdmin)