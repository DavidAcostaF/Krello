from django.urls import path
from apps.workspace import views
urlpatterns = [
    path('',views.Home.as_view())
]