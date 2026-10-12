from django.shortcuts import render

from storage import load_publications


def publications(request):
    """Список публикаций."""
    context = {
        "publications": load_publications(
            "data/publications.json",
        ),
    }
    return render(
        request, "publications_app/publication_list.html", context,
    )
