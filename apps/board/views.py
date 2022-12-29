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
            

class EditCard(DetailView):
    model = Card
    #fields = ['title','description']
    template_name = 'board/edit_card_modal.html'

    # def get(self, request,id, *args, **kwargs,):
    #     card = self.get_object()
    #     context = {
    #         'card':card
    #     }
    #     return render(request, self.template_name,context)

    # def get_queryset(self):
    #     query = super().get_queryset()
    #     query = query.filter(id=self.kwargs['id'])
    #     return query 