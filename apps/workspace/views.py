from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from apps.workspace import models
# Create your views here.

# class Home(TemplateView):
#     template_name = 'home.html'

class ListsWorkspaces(ListView):
    model = models.Workspace
    template_name = 'home_boards/home_boards.html'

    def get_query_set(self):
        user = self.request.user
        query = self.model.objects()
