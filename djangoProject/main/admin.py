from django.contrib import admin
from main.models.todo import Todo
from main.models.todo_list import TodoList


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'owner')
    search_fields = ['name', 'owner']
    list_display = ('name', 'owner', 'created', 'due')


@admin.register(TodoList)
class ListAdmin(admin.ModelAdmin):
    search_fields = ['name', 'favorite']
