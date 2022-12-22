from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView  
from .models import Board,Column,Card
# Create your views here.

class BoardListView(ListView):
    model = Board
    template_name = 'board/board.html'

    def get(self, request,id,title, *args, **kwargs,):
        board = Board.objects.get(id=id)
        context = {}
        print(board.title == title)
        if board.title == title:
            columns = Column.objects.filter(board=board)
            cards = Card.objects.filter(column__in=columns)
            context['columns'] = columns
            context['cards'] = cards
            context['board'] = board
            return render(request, self.template_name,context)
            
class CreateColums(CreateView):
    model = Column

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        board = request.POST.get('board')
        board = Board.objects.get(id=board)
        column = Column.objects.create(title=title,board=board)
        column.save()
        return render(request, 'board/board.html')