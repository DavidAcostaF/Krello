from rest_framework import serializers
from apps.board.models import Board,Column,Card

class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = ('title','board')



class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title','column')

class SaveDescriptionSerializer(serializers.Serializer):
    card = serializers.DjangoModelField()
    description = serializers.CharField()

class SaveDescriptionSerializer(serializers.Serializer):
    card = serializers.DjangoModelField()
    description = serializers.CharField()

class editColumnTitleSerializer(serializers.Serializer):
    title = serializers.CharField()