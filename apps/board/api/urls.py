from rest_framework import routers
from django.urls import path
from apps.board.api.api import CreateColumnApi

# router = routers.DefaultRouter()
# router.register('create-column',CreateColumnApi)

urlpatterns = [
    path('create-column/<int:pk>',CreateColumnApi.as_view(),name='create_column')
]

# urlpatterns = router.urls