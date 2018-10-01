from rest_framework.serializers import ModelSerializer
from Serializers.models import Serializers

class SerializersSerializer(ModelSerializer):
    class Meta:
        model = Serializers
        fields = ('id', 'nome', 'descricao','aprovado')