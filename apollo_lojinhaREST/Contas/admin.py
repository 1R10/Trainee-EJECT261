from django.contrib import admin
from Contas.models import ContaPadrao

class ContaPadraoAdmin(admin.ModelAdmin):
    list_display = ('role',
                    'nome_completo', 
                    'nascimento', 
                    'cpf',
                    #'email', 
                    #'senha', 
                    'telefone', 
                    'cep', 
                    'endereco', )
    
    list_display_links = ('role', 'nome_completo',)
    list_per_page      = 20
    search_fields      = ('nome_completo',)

admin.site.register(ContaPadrao,ContaPadraoAdmin)