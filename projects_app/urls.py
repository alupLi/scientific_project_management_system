from django.urls import path
from . import views

app_name = "projects_app"

urlpatterns = [
    path("", views.projects, name="projects"),
    path("create/", views.project_create, name="project_create"),

    # Маршруты задач — ДО динамического slug
    path(
        "<slug:slug>/tasks/create/",
        views.task_create,
        name="task_create",
    ),
    path(
        "<slug:slug>/tasks/<int:task_id>/edit/",
        views.task_edit,
        name="task_edit",
    ),
    path(
        "<slug:slug>/tasks/<int:task_id>/delete/",
        views.task_delete,
        name="task_delete",
    ),

    # Маршруты проекта
    path("<slug:slug>/", views.project_detail, name="project_detail"),
    path("<slug:slug>/edit/", views.project_edit, name="project_edit"),
    path("<slug:slug>/delete/", views.project_delete, name="project_delete"),
]
