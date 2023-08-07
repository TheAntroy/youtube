from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
# Create your views here.

def index(request):
    context = {
        'todos': Todo.objects.all().order_by('-id')
    }
    return render(request,'todo/index.html', context)

def insert_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todo/list/')

def delete_item(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todo/list/')