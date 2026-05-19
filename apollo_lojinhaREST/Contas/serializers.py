from rest_framework import serializers
from Contas.models import ContaPadrao

class ContaPadraoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContaPadrao
        fields = '__all__'