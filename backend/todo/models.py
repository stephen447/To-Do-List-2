from django.db import models
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Create your models here.
class Todoitem(models.Model):
    title = models.CharField(default = "", max_length=30)
    description = models.CharField(default = "", max_length=50, null=True)
    complete = models.BooleanField(default=False)
    completed_by = models.DateField(null=True)
