from django.urls import path
from apps.board.views import BoardListView

urlpatterns = [
    path('<int:id>/<str:title>/',BoardListView.as_view(),name='board_view'),
    # path('create-column/<int:id>',CreateColums.as_view(),name='create_column')
]