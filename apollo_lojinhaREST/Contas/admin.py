from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from Contas.models import ContaPadrao

'''class CadastrarUserAdmin(admin.ModelAdmin):
    list_display = ('role',
                    'nome_completo', 
                    'nascimento', 
                    'cpf',
                    'email', 
                    'senha', 
                    'telefone', 
                    'cep', 
                    'endereco', )
    
    list_display_links = ('role', 'nome_completo',)
    list_per_page      = 20
    search_fields      = ('nome_completo',)

admin.site.register(ContaPadrão, CadastrarUserAdmin)'''

admin.site.register(ContaPadrao)