from django.shortcuts import render

from db import queries


def researchers(request):
    """Список исследователей из БД."""
    context = {
        "researchers": queries.get_all_researchers(),
    }
    return render(
        request, "researchers_app/researcher_list.html", context,
    )


def statistics(request):
    """Статистика: количество задач у исследователей."""
    context = {
        "stats": queries.get_researcher_stats(),
    }
    return render(
        request, "researchers_app/statistics.html", context,
    )
