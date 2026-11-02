from django.shortcuts import render
from publications_app.models import Publication


def publications(request):
    """Список публикаций из БД."""
    context = {
        "publications": Publication.objects.all(),
    }
    return render(
        request, "publications_app/publication_list.html", context,
    )
