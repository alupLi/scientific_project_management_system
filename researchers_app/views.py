from django.shortcuts import render
from django.db.models import Count
from researchers_app.models import Researcher


def researchers(request):
    """Список исследователей из БД."""
    context = {
        "researchers": Researcher.objects.all(),
    }
    return render(
        request, "researchers_app/researcher_list.html", context,
    )


def statistics(request):
    """Статистика: количество задач у исследователей."""
    # Аннотируем исследователей количеством их задач
    stats = Researcher.objects.annotate(
        task_count=Count("tasks")
    ).order_by("-task_count")

    context = {
        "stats": stats,
    }
    return render(
        request, "researchers_app/statistics.html", context,
    )
