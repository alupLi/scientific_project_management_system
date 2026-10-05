from django.urls import path

from . import views

urlpatterns = [
    path("", views.researchers, name="researchers"),
]
