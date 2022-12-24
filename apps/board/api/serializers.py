from rest_framework import serializers
from apps.board.models import Board,Column,Card

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = 'id'