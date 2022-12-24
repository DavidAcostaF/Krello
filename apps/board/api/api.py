from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.http import HttpResponse
from .serializers import ColumnSerializer
from apps.board.models import Board,Column,Card


class CreateColumnApi(CreateAPIView):
    # queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def post(self, request,pk):
        title = request.data.get('title')
        board = Board.objects.get(id=pk)
        if board and title:
            column = Column.objects.create(title=title,board=board)
            column.save()
        return Response(status = 200)