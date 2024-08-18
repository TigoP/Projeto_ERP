from common.models import Endereco
from common.serializers import EnderecoSerializer
from rest_framework import viewsets

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer = EnderecoSerializer
