from django.shortcuts import render

from db import queries


def projects(request):
    """Список проектов (с поддержкой поиска)."""
    query = request.GET.get("search", "").strip()

    if query:
        projects_list = queries.search_projects(query)
    else:
        projects_list = queries.get_all_projects()

    context = {
        "projects": projects_list,
        "search_query": query,
    }
    return render(
        request, "projects_app/project_list.html", context,
    )


def project_detail(request, project_id):
    """Карточка проекта с задачами и источниками."""
    project = queries.get_project_by_id(project_id)

    if project is None:
        return render(
            request,
            "projects_app/project_detail.html",
            {"project": None},
            status=404,
        )

    tasks = queries.get_tasks_for_project(project_id)
    publications = queries.get_publications_for_project(project_id)

    context = {
        "project": project,
        "tasks": tasks,
        "publications": publications,
    }
    return render(
        request, "projects_app/project_detail.html", context,
    )
