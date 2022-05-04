import http

from main.models.todo import Todo
from main.serializers.todo import TodoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def get_todos_by_todo_list(request, todo_list_id):
    todos = Todo.todo_related.filter(todo_list_id=todo_list_id)
    serializer = TodoSerializer(todos, many=True)
    if todos is None:
        return http.HTTPStatus('No todo list found with given todo_list_id')
    return JsonResponse(data=serializer.data, safe=False)
