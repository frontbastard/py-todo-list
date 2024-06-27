from django.urls import path

from tasks.views.tag_views import TagListView
from tasks.views.task_views import TaskListView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
]
