import http

from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def todo_list(request, list_id):
    todos = Todo.objects.all().filter(is_done=False, list_id=list_id)
    data = {
        'todos': todos,
        'list_id': list_id
    }
    return render(request, 'main/todo_list.html', data)


@csrf_exempt
def todo_list_toggle_done(request, list_id, todo_id):
    is_done = request.POST["is_done"]
    todo = Todo.objects.get(is_done=is_done, list_id=list_id, id=todo_id)
    print(is_done)
    todo.is_done = not todo.is_done
    print(todo.is_done)
    todo.save()
    return HttpResponse(http.HTTPStatus.ACCEPTED)


@csrf_exempt
def completed_todo_list(request, list_id):
    todos = Todo.objects.all().filter(is_done=True, list_id=list_id)
    data = {
        'todos': todos,
        'list_id': list_id
    }
    return render(request, 'main/completed_todo_list.html', data)
