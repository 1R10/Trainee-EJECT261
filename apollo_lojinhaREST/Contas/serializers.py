from rest_framework import serializers
from Contas.models import ContaPadrao

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