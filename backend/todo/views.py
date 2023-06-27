from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodolistSerializer, CreateTodolistSerializer, CompleteTodolistSerializer
from .models import Todoitem

from django.http import JsonResponse

# Create your views here.
class TodolistView(APIView):
    serializer_type = CreateTodolistSerializer
    def post(self, request, format = None):
        print("hello")
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_type(data = request.data)
        if serializer.is_valid():
            print("Form data is okay")
            print(request.data)
            title = serializer.data.get("title")
            print("title", title)
            description = serializer.data.get('description')
            complete = serializer.data.get('complete')
            completed_by = serializer.data.get('completed_by')
            todoitem = Todoitem(title=title, description=description, complete=complete, completed_by=completed_by)
            todoitem.save()
            return Response(TodolistSerializer(todoitem).data, status=status.HTTP_201_CREATED)
        return Response("Error: Invalid request!", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        list = Todoitem.objects.all().order_by('complete')
        if len(list)>0:
            data = TodolistSerializer(list, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response("No items in your to do list", status=status.HTTP_200_OK)
    
    def put(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = CompleteTodolistSerializer(data=request.data)
        if serializer.is_valid():
            id = request.GET.get('id')
            complete = request.GET.get('complete')

            if complete=="true":
                complete=True
            elif complete=="false":
                complete=False

            item = Todoitem.objects.filter(id=id).update(complete=complete)
            return Response("State updated correctly", status=status.HTTP_200_OK)
        return Response("Error: Invalid request!", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        id = request.GET.get('id')
        item = Todoitem.objects.filter(id=id)
        if item:
            item.delete()
            return Response("Item deleted sucessfully", status=status.HTTP_200_OK)
        return Response("No item found", status=status.HTTP_204_NO_CONTENT)
            


