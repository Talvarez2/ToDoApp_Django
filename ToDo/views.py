from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Todo


def index(request):
    todo_list = Todo.objects.order_by('-added_date')
    return render(request, 'ToDo/index.html', {'todo_list': todo_list})


@require_POST
def add_todo(request):
    text = request.POST.get('text', '').strip()
    if text:
        Todo.objects.create(added_date=timezone.now(), text=text)
    return HttpResponseRedirect(reverse('todo:index'))


@require_POST
def delete_todo(request, todo_id):
    get_object_or_404(Todo, id=todo_id).delete()
    return HttpResponseRedirect(reverse('todo:index'))
