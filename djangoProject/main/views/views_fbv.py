import http
import logging

from main.models.todo import Todo
from main.serializers.todo import TodoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_todos_by_todo_list(request, todo_list_id):
    todos = Todo.todo_related.filter(todo_list_id=todo_list_id)
    serializer = TodoSerializer(todos, many=True)
    if todos is None:
        logger.error("No todo list found with given todo_list_id")
        return JsonResponse({}, status=http.HTTPStatus.NOT_FOUND)
    logger.error("OK")
    return JsonResponse(data=serializer.data, safe=False)
