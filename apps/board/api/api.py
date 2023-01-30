from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView
from django.http import HttpResponse
from .serializers import ColumnSerializer, SaveDescriptionSerializer
from apps.board.models import Board, Column, Card


class CreateColumnApi(CreateAPIView):
    # queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def post(self, request, pk):
        # esto funciona como un form
        # board = Board.objects.get(id=pk)
        # colunm = ColumnSerializer(data=request.data,board=board)
        # print
        # if colunm.is_valid():
        #     colunm.save()
        # return Response(status = 200)
        title = request.data.get('title')
        board = Board.objects.get(id=pk)
        if board and title:
            column = Column.objects.create(title=title, board=board)
            column.save()
            response = {
                'id': column.id,
                'title': column.title,
            }
        return Response(response,status=200)


class CreateCardApi(CreateAPIView):
    

    def post(self, request, pk):
        title = request.data.get('title')
        column = Column.objects.get(id=pk)
        if column and title:
            card = Card.objects.create(title=title, column=column)
            card.save()
            return Response({'title': card.id}, status=200)
        return Response(status=200)


class MoveCard(CreateAPIView):

    def post(self, request, pk):
        card = Card.objects.get(id=pk)
        column_id = request.data.get('column_id')
        column = Column.objects.get(id=column_id)
        if card and column:
            card.column = column
            card.save()
            return Response(status=200)
        return Response(status=400)


class SaveDecriptionCard(CreateAPIView):
    model = Card
    serializer_class = SaveDescriptionSerializer

    def post(self, request, pk):
        card = Card.objects.get(id=pk)
        description = request.data.get('description')
        data = {
            'card': card,
            'description': description
        }
        serializer = SaveDescriptionSerializer(data=data)
        if serializer.is_valid():
            card.description = serializer.validated_data['description']
            card.save()
            print(card.description)
            return Response(status=200)
        return Response(status=400)


class addBoardToFavorite(UpdateAPIView):
    model = Board
    def put(self, request, pk):
        board = Board.objects.get(id=pk)
        print(board.favorite)
        # if board.favorite != True:
        #     board.favorite = True
        # else:
        #     board.favorite = False
        board.favorite = not board.favorite
        board.save()
        return Response(status=200)


class EditTitleColumn(UpdateAPIView):
    model = Column
    def put(self, request, pk):
        column = Column.objects.get(id=pk)
        title = request.data.get('title')
        if column and title:
            column.title = title
            column.save()
            return Response(status=200)
        return Response(status=400)