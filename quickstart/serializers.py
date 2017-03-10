from rest_framework import serializers

from . import models


class RoomSerializer(serializers.ModelSerializer):
    """ Room Serializer View"""

    class Meta:
        model = models.Room
        exclude = ('id',)


class RoomCreateSerializer(serializers.ModelSerializer):
    """ Room Serializer View"""

    class Meta:
        model = models.Room
        exclude = ('hostel',)
