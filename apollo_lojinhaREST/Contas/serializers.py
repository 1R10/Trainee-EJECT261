from rest_framework import serializers
from Contas.models import ContaPadrao
from .Validador_CPF import cpf_valido

class ContaPadraoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContaPadrao
        exclude = [
                'username',
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
        if not cpf_valido(str(dados['cpf'])):
            raise serializers.ValidationError({'cpf':'CPF inválido.'}) 
        
        if not str(dados['nome_completo']).isalpha():
            raise serializers.ValidationError({'nome_completo': 'O nome só pode conter letras.'})
        if len(dados['telefone']) != 11:
            raise serializers.ValidationError({'telefone': 'Telefone deve conter 13 dígitos.'})
        if not str(dados['cep']).isdigit():
            raise serializers.ValidationError({'cep': 'CEP inválido. Insira apenas números.'})


        return dados