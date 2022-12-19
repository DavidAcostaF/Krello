from django.urls import path
from apps.workspace import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('boards',views.ListsWorkspaces.as_view(),name='home_boards')
]