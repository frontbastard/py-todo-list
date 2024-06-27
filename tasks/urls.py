from django.urls import path

from tasks.views.tag_views import (
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView
)
from tasks.views.task_views import TaskListView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
