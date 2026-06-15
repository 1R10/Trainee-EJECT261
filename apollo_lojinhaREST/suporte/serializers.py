from rest_framework import serializers
from suporte.models import ContatarSuporte

class SuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ContatarSuporte
        fields = '__all__'