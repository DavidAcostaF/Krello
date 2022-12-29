from django.urls import path
from apps.board.views import BoardListView,EditCard

urlpatterns = [
    path('<int:id>/<str:title>/',BoardListView.as_view(),name='board_view'),
    path('edit_card/<int:pk>/',EditCard.as_view(),name='edit_card'),
]