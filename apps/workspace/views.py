from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from apps.workspace.models import Workspace
from apps.board.models import Board
# Create your views here.

class Home(TemplateView):
    template_name = 'home_page/home.html'

class ListsWorkspaces(ListView):
    model = Workspace
    template_name = 'home_boards/home_boards.html'

    def get(self,request):
        list_boards = []
        user = self.request.user
        workspaces = Workspace.objects.filter(created_by = user)
        for workspace in workspaces:
            list_boards.append(Board.objects.filter(workspace=workspace))
        print(list_boards)
        context = {
            'workspaces':workspaces,
            'list_workspaces':list_boards,
        }
        return render(request,'home_page/home_boards.html',context)
