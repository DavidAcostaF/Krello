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
        #esto funciona como un form
        # board = Board.objects.get(id=pk)
        # colunm = ColumnSerializer(data=request.data,board=board)
        # print
        # if colunm.is_valid():
        #     colunm.save()
        # return Response(status = 200)
        title = request.data.get('title')
        board = Board.objects.get(id=pk)
        if board and title:
            column = Column.objects.create(title=title,board=board)
            column.save()
        return Response(status = 200)

class CreateCardApi(CreateAPIView):

    def post(self, request,pk):
        title = request.data.get('title')
        column = Column.objects.get(id=pk)
        if column and title:
            column = Card.objects.create(title=title,column=column)
            column.save()
            return Response({'card':column},status = 200)
        return Response(status = 200)