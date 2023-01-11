from rest_framework import routers
from django.urls import path
from apps.board.api.api import CreateColumnApi,CreateCardApi,MoveCard,SaveDecriptionCard

# router = routers.DefaultRouter()
# router.register('create-column',CreateColumnApi)

urlpatterns = [
    path('create-column/<int:pk>',CreateColumnApi.as_view(),name='create_column'),
    path('create-card/<int:pk>',CreateCardApi.as_view(),name='create_card'),
    path('move-card/<int:pk>',MoveCard.as_view(),name='move_card'),
    path('save-description-card/<int:pk>',SaveDecriptionCard.as_view(),name='save_description'),
]

# urlpatterns = router.urls