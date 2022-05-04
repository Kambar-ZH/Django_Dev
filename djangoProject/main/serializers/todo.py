from rest_framework.serializers import ModelSerializer
from main.models.todo import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
