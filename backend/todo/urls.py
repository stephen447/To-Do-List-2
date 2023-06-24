from django.urls import path
from .views import TodolistView
urlpatterns = [
    path('todo', TodolistView.as_view())
]