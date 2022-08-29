from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Marcas, Carro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcasSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = "__all__"
    
class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"