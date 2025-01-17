from django.urls import path

from tasks.views.tag_views import (
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView
)
from tasks.views.task_views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleCompletionView,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle-completion/",
        TaskToggleCompletionView.as_view(),
        name="task-toggle-completion"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
