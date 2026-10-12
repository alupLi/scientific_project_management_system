from django.shortcuts import render

from storage import load_researchers


def researchers(request):
    """Список исследователей."""
    context = {
        "researchers": load_researchers(
            "data/researchers.json",
        ),
    }
    return render(
        request, "researchers_app/researcher_list.html", context,
    )
