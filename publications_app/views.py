from django.http import HttpResponse

from homepage.views import page
from storage import load_publications


def publications(request):
    """Список публикаций."""
    publications_list = load_publications("data/publications.json")

    if not publications_list:
        content = "<h1>Публикации</h1><p>Публикаций пока нет.</p>"
        return HttpResponse(page("Публикации", content))

    items = ""
    for pub in publications_list:
        items += (
            f'<li class="list-group-item">'
            f'{pub.title} — {pub.journal} ({pub.date})'
            f'</li>'
        )

    content = f"""
    <h1>Публикации</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Публикации", content))
