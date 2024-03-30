from django.shortcuts import render, redirect
from django.contrib import messages

# import form module
from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("_date")
