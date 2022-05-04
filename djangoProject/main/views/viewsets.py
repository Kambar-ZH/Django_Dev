from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models.todo import Todo
from main.models.todo_list import TodoList
from main.serializers.todo import TodoSerializer
from main.serializers.todo_list import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
