from rest_framework import serializers
from Contas.models import ContaPadrao
from .Validador_CPF import cpf_valido

class ContaPadraoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContaPadrao
        exclude = [
                #'username', deu bronca
                'user_permissions',
                'groups', 
                'first_name',
                'last_name',
                'is_superuser', 
                'is_staff',
                'last_login',
                'is_active',
                'date_joined']
        
    def validate_cpf(self, cpf): 
        if cpf_valido(cpf) == False:
            raise serializers.ValidationError('CPF inválido.') 
        return cpf