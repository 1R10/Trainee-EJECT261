from rest_framework import serializers
from Contas.models import ContaPadrao
from .validators import cpf_valido, telefone_valido, cep_valido, nome_valido
from django.contrib.auth.password_validation import validate_password
from .encontraCEP import buscar_endereco


class ContaPadraoSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        validate_password(dados['password']) # isso lê as regras do settings
        if not cpf_valido(str(dados['cpf'])):
            raise serializers.ValidationError({'cpf':'CPF inválido.'}) 
        
        if not nome_valido(dados['nome_completo']):
            raise serializers.ValidationError({'nome_completo': 'O nome só pode conter letras.'})
        if not telefone_valido(dados['telefone']):
            raise serializers.ValidationError({'telefone': 'Telefone deve conter formato 00 00000-0000.'})
        if not cep_valido(dados['cep']):
            raise serializers.ValidationError({'cep': 'CEP inválido. Formato 12345678.'})
        if cep_valido(dados['cep']):
            dados['endereco'] = buscar_endereco(dados['cep'])


        return dados
    
    def create(self,dados):
        dados['username'] = dados['email']
        conta = ContaPadrao.objects.create_user(**dados)
        return conta