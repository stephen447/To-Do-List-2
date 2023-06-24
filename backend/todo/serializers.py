from rest_framework import serializers
from .models import Todoitem

class TodolistSerializer(serializers.ModelSerializer):
    class meta:
        model = Todoitem
        fields = ['id', 'title', 'description', 'complete', 'completed_by']

class CreateTodolistSerializer(serializers.Serializer):
    class meta:
        model = Todoitem
        fields = ['id', 'title', 'description', 'completed_by']