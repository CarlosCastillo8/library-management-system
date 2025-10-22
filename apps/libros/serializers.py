from rest_framework import serializers
from .models import Autor, Titulo, Ejemplar

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class TituloSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Titulo
        fields = '__all__'


class EjemplarSerializer(serializers.ModelSerializer):
    titulo = TituloSerializer(read_only=True)

    class Meta:
        model = Ejemplar
        fields = '__all__'
