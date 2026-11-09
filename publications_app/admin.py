from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "journal", "date")
    list_display_links = ("title",)
    search_fields = ("title", "journal")
    list_filter = ("journal", "date")
    ordering = ("-date",)
    list_per_page = 20
