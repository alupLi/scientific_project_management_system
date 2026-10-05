from django.http import HttpResponse

from homepage.views import page

from storage import (
    load_projects, load_researchers,
    load_publications,
)


def projects(request):
    """Список проектов."""
    researchers = load_researchers("data/researchers.json")
    publications = load_publications("data/publications.json")
    projects_list = load_projects(
        "data/projects.json", researchers, publications,
    )

    if not projects_list:
        content = "<h1>Проекты</h1><p>Проектов пока нет.</p>"
        return HttpResponse(page("Проекты", content))

    items = ""
    for p in projects_list:
        items += (
            f'<li class="list-group-item">'
            f'<a href="/projects/{p.id}/">{p.name}</a> '
            f'— задач: {len(p.tasks)}, '
            f'источников: {len(p.references)}'
            f'</li>'
        )

    content = f"""
    <h1>Проекты</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Проекты", content))


def project_detail(request, project_id):
    """Карточка проекта."""
    researchers = load_researchers("data/researchers.json")
    publications = load_publications("data/publications.json")
    projects_list = load_projects(
        "data/projects.json", researchers, publications,
    )

    project = next(
        (p for p in projects_list if p.id == project_id),
        None,
    )

    if project is None:
        content = """
        <h1 class="text-danger">Проект не найден</h1>
        <a href="/projects/" class="btn btn-outline-secondary">
            ← к списку проектов
        </a>
        """
        return HttpResponse(
            page("Проект не найден", content), status=404,
        )

    tasks_html = ""
    for t in project.tasks:
        researcher = t.researcher.name if t.researcher else "—"
        tasks_html += (
            f'<li class="list-group-item">'
            f'{t.task_name} — {researcher} '
            f'(до {t.deadline}) [{t.status}]'
            f'</li>'
        )
    if not tasks_html:
        tasks_html = '<li class="list-group-item">Задач нет</li>'

    refs_html = ""
    for pub in project.references:
        refs_html += (
            f'<li class="list-group-item">'
            f'{pub.title} — {pub.journal} ({pub.date})'
            f'</li>'
        )
    if not refs_html:
        refs_html = '<li class="list-group-item">Источников нет</li>'

    content = f"""
    <h1>{project.name}</h1>
    <p><strong>ID:</strong> {project.id}</p>
    <p><strong>Сроки:</strong> {project.start} — {project.end}</p>

    <h3 class="mt-4">Задачи</h3>
    <ul class="list-group">{tasks_html}</ul>

    <h3 class="mt-4">Источники</h3>
    <ul class="list-group">{refs_html}</ul>

    <a href="/projects/" class="btn btn-outline-secondary mt-3">
        ← к списку проектов
    </a>
    """
    return HttpResponse(page(project.name, content))
