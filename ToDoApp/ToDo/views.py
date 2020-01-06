from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Todo

def index(request):
    todo_list = Todo.objects.order_by('-added_date')
    return render(request, 'ToDo/index.html', {'todo_list': todo_list})


def add_todo(request):
    added_date = timezone.now()
    text = request.POST['text']
    todoItem = Todo(added_date=added_date, text=text)
    todoItem.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todo:index'))

