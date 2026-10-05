from django.http import HttpResponse

from homepage.views import page
from storage import load_researchers


def researchers(request):
    """Список исследователей."""
    researchers_list = load_researchers("data/researchers.json")

    if not researchers_list:
        content = (
            "<h1>Исследователи</h1>"
            "<p>Исследователей пока нет.</p>"
        )
        return HttpResponse(page("Исследователи", content))

    items = ""
    for r in researchers_list:
        items += (
            f'<li class="list-group-item">'
            f'[{r.id}] {r.name} — {r.field}'
            f'</li>'
        )

    content = f"""
    <h1>Исследователи</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Исследователи", content))
