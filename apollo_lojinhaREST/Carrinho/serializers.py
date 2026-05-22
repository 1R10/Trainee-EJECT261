from rest_framework import serializers
from .models import Carrinho

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Carrinho
        fields = '__all__'

       #6:00 https://cursos.alura.com.br/course/django-rest-framework-construindo-apis-restful-zero/task/159566