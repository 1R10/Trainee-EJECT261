from rest_framework import serializers
from Contas.models import ContaPadrao

class ContaPadraoSerializer(serializers.ModelSerializer):
    class meta: 
        model = ContaPadrao
        fields = '__all__'