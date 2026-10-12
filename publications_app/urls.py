from django.urls import path
from . import views

app_name = "publications_app"

urlpatterns = [
    path("", views.publications, name="publications"),
]
