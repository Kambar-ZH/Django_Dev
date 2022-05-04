import http

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from main.models.todo import Todo
from main.serializers.todo import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, list_id):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class CompletedListView(APIView):

    def get(self, request, list_id):
        todos = Todo.objects.all().filter(list_id=list_id, is_done=True)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodoView(APIView):
    def post(self, request, list_id, todo_id):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http.HTTPStatus.CREATED)
        return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)
