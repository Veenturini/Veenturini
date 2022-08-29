from rest_framework.viewsets import ModelViewSet

from core.models import Carro, Categoria, Carro,  Marcas
from core.serializers import CategoriaSerializer, MarcasSerializer, CarroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcasViewSet(ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer