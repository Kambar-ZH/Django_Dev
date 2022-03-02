import json

from django.shortcuts import render


# Create your views here.
def todo_list(request):
    f = open('/home/kambar/PycharmProjects/djangoProject/main/db/layout_data.json')
    data = json.load(f)
    f.close()
    return render(request, 'main/todo_list.html', data)


def completed_todo_list(request):
    data = {
        'table': {
            'headers': ['Task', 'Created', 'Due on', 'Owner', 'Mark'],
            'rows': [
                {'Task': 'Task0', 'Created': '10/09/2018', 'DueOn': '12/09/2018', 'Owner': 'admin', 'Mark': 'not done'},
            ]
        },
    }
    return render(request, 'main/completed_todo_list.html', data)
