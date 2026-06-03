from rest_framework import serializers
from Contas.models import ContaPadrao
from .Validador_CPF import cpf_valido

class ContaPadraoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContaPadrao
        exclude = [
                'username'
                'user_permissions',
                'groups', 
                'first_name',
                'last_name',
                'is_superuser', 
                'is_staff',
                'last_login',
                'is_active',
                'date_joined']
        
    def validate(self, dados): 
        if cpf_valido(dados['cpf']) == False:
            raise serializers.ValidationError({'cpf':'CPF inválido.'}) 
        
        if not dados['nome_completo'.isalpha()]:
            raise serializers.ValidationError({'nome_completo': 'O nome só pode conter letras.'})
        if len(dados['telefone']) != 13:
            raise serializers.ValidationError({'telefone': 'Telefone deve conter 13 dígitos.'})
        return dados