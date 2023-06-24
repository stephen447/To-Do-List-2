from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodolistSerializer, CreateTodolistSerializer
from .models import Todoitem

from django.http import JsonResponse

# Create your views here.
class TodolistView(APIView):
    serializer_type = CreateTodolistSerializer()
    def post(self, request, format = None):
        serializer = self.serializer_type(data = request.data)
        if serializer.is_valid():
            title = serializer.data.get("title")
            description = serializer.data.get('description')
            complete = serializer.data.get('complete')
            completed_by = serializer.data.get('completed_by')
            todoitem = Todoitem(title=title, description=description, complete=complete, completed_by=completed_by)
            todoitem = todoitem.save()
            return Response(TodolistSerializer(todoitem).data, status=status.HTTP_201_CREATED)
        return Response("Error: Invalid request!", status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        list = Todoitem.objects.all()
        if len(list)>0:
            return Response(list, status=status.HTTP_200_OK)
        return Response("No items in your to do list", status=status.HTTP_200_OK)
