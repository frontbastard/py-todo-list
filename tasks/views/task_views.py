from django.views import generic

from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task

