from django.shortcuts import render

from db import queries


def publications(request):
    """Список публикаций из БД."""
    context = {
        "publications": queries.get_all_publications(),
    }
    return render(
        request, "publications_app/publication_list.html", context,
    )
