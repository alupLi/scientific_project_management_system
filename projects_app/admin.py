from django.contrib import admin, messages
from django.db.models import Count
from .models import Project, Task


class TaskInline(admin.TabularInline):
    """Позволяет просматривать задачи внутри карточки проекта."""
    model = Task
    fields = ("task_name", "researcher", "deadline", "status")
    extra = 0
    can_delete = False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "start", "end",
        "tasks_count", "status"
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status", "start")
    ordering = ("name",)
    list_per_page = 20
    inlines = (TaskInline,)

    def get_queryset(self, request):
        # Аннотируем количество задач (оптимизация запросов)
        qs = super().get_queryset(request)
        return qs.annotate(
            tasks_count=Count("tasks")
        )

    @admin.display(description="Задач", ordering="tasks_count")
    def tasks_count(self, obj):
        return obj.tasks_count


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "task_name", "project", "researcher", "deadline", "status")
    list_display_links = ("task_name",)
    search_fields = ("task_name", "project__name", "researcher__name")
    list_filter = ("status", "deadline")
    list_select_related = ("project", "researcher")
    ordering = ("deadline",)
    list_per_page = 20
    autocomplete_fields = ("project", "researcher")
    readonly_fields = ("id",)
    date_hierarchy = "deadline"

    @admin.action(description="Отметить выбранные задачи как завершенные")
    def mark_completed(self, request, queryset):
        updated = queryset.update(status=Task.Status.COMPLETED)
        self.message_user(
            request, 
            f"Завершено задач: {updated}.", 
            messages.SUCCESS
        )

    actions = ("mark_completed",)
