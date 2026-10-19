from django.urls import path
from . import views

app_name = "researchers_app"

urlpatterns = [
    path("", views.researchers, name="researchers"),
    path("statistics/", views.statistics, name="statistics"),
]
