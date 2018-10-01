# permite fazer create(), retrive(), uodate(), partial_update(), destroy(), list()
from rest_framework.viewsets import ModelViewSet
from Serializers.models import Serializers
from .serializers import SerializersSerializer


class SerializersViewSet(ModelViewSet):
    queryset = Serializers.objects.all() # pega todos do banco de dados
    serializer_class = SerializersSerializer # como voce vai mostrar  esse dado
                                         # quais os campos que voce que inclua no json