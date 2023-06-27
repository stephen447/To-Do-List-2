from rest_framework import serializers
from .models import Todoitem

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ['id', 'title', 'description', 'complete', 'completed_by']

class CreateTodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ['id', 'title', 'description', 'complete', 'completed_by']

class CompleteTodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ['id', 'complete']