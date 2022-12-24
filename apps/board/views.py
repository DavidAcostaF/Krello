from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView  
from .models import Board,Column,Card
from django.http import HttpResponse
# Create your views here.

class BoardListView(ListView):
    model = Board
    template_name = 'board/board.html'

    def get(self, request,id,title, *args, **kwargs,):
        board = Board.objects.get(id=id)
        context = {}
        if board.title == title:
            columns = Column.objects.filter(board=board)
            cards = Card.objects.filter(column__in=columns)
            context['columns'] = columns
            context['cards'] = cards
            context['board'] = board
            return render(request, self.template_name,context)
            
# class CreateColums(CreateView):
#     model = Column

#     def post(self, request,id, *args, **kwargs):
#         title = request.POST.get('title')
#         print(title['title'])
#         # board = request.POST.get('board')
#         board = Board.objects.get(id=id)
#         if board and title:
#             column = Column.objects.create(title=title,board=board)
#             column.save()
#         return HttpResponse(status = 200)