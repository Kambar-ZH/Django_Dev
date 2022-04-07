import http

from ..models import Todo, List
from ..serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def get_todo_list(request, list_id):
    todos = Todo.objects.all().filter(is_done=False, list_id=list_id)
    serializer = TodoSerializer(todos, many=True)
    todo_list = List.objects.get(id=list_id)
    if todo_list is None:
        return http.HTTPStatus('No list available with given list_id')
    return JsonResponse(data=serializer.data, safe=False)


@csrf_exempt
def post_todo(request, list_id, todo_id):
    if request.method == "PUT":
        todo = Todo.objects.get(id=todo_id, list_id=list_id)
        todo.is_done = not todo.is_done
        todo.save()
        return JsonResponse(status=http.HTTPStatus.ACCEPTED)

    return JsonResponse(status=http.HTTPStatus.SERVICE_UNAVAILABLE)


@csrf_exempt
def get_completed_todo_list(request, list_id):
    todos = Todo.objects.all().filter(is_done=True, list_id=list_id)
    todo_list = List.objects.get(id=list_id)
    serializer = TodoSerializer(todos, many=True)
    if todo_list is None:
        return http.HTTPStatus('No list available with given list_id')
    return JsonResponse(data=serializer.data, safe=False)
