from rest_framework import routers
from django.urls import path
from apps.board.api import api

# router = routers.DefaultRouter()
# router.register('create-column',CreateColumnApi)

urlpatterns = [
    path('create-column/<int:pk>',api.CreateColumnApi.as_view(),name='create_column'),
    path('create-card/<int:pk>',api.CreateCardApi.as_view(),name='create_card'),
    path('move-card/<int:pk>',api.MoveCard.as_view(),name='move_card'),
    path('save-description-card/<int:pk>',api.SaveDecriptionCard.as_view(),name='save_description'),
    path('add-board-to-favorite/<int:pk>',api.addBoardToFavorite.as_view(),name='add_board_to_favorite'),
    path('edit-column-title/<int:pk>',api.EditColumnTitle.as_view(),name='edit_column_title'),
]

# urlpatterns = router.urls