from django.shortcuts import render

from storage import (
    load_projects, load_researchers, load_publications,
)


def _load_all():
    """Загружает проекты со связанными объектами."""
    researchers = load_researchers("data/researchers.json")
    publications = load_publications("data/publications.json")
    return load_projects(
        "data/projects.json", researchers, publications,
    )


def projects(request):
    """Список проектов."""
    context = {
        "projects": _load_all(),
    }
    return render(
        request, "projects_app/project_list.html", context,
    )


def project_detail(request, project_id):
    """Карточка проекта."""
    projects_list = _load_all()
    project = next(
        (p for p in projects_list if p.id == project_id),
        None,
    )
    context = {
        "project": project,
    }
    return render(
        request,
        "projects_app/project_detail.html",
        context,
        status=404 if project is None else 200,
    )
