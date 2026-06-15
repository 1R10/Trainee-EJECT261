from rest_framework import serializers
from Pedidos.models import PedidoModel

class PedidoSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = PedidoModel
        exclude = []

        def validate(self, dados):
                '''
                Ainda não há dados a serem validados ainda
                '''
                return dados