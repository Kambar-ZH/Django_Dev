from rest_framework.serializers import ModelSerializer
from main.models.todo_list import TodoList


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'