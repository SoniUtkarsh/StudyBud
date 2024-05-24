from rest_framework.serializers import ModelSerializer
from studybud.models import Room


class RoomsSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
