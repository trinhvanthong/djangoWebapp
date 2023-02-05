from .models import *
from rest_framework.serializers import ModelSerializer

class PaintingSerializer(ModelSerializer):
    class Meta:
        model = Paintings
        fields =["id", "name","Author","price","size"]