from django.urls import path
from . import views

app_name = "projects_app"

urlpatterns = [
    path("", views.projects, name="projects"),
    path("<int:project_id>/", views.project_detail,
         name="project_detail"),
]
