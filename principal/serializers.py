from rest_framework import serializers
from principal.models import Publicacao

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__'

