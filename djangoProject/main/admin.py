from django.contrib import admin
from .models import Todo, List


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'owner')
    search_fields = ['name', 'owner']
    list_display = ('name', 'owner', 'created_at', 'due_on')


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    search_fields = ['name']
