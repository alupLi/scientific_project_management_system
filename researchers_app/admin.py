from django.contrib import admin
from .models import Researcher


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "field")
    list_display_links = ("name",)
    search_fields = ("name", "field")
    ordering = ("name",)
    list_per_page = 20
