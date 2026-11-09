from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from projects_app.models import Project


def projects(request):
    """Список проектов (с поддержкой поиска и пагинацией)."""
    query = request.GET.get("search", "").strip()
    sort = request.GET.get("sort", "name")

    projects_list = Project.objects.all()

    if query:
        projects_list = projects_list.filter(name__icontains=query)

    projects_list = projects_list.annotate(
        tasks_count=Count("tasks", distinct=True),
        refs_count=Count("references", distinct=True)
    )

    sort_fields = {
        "name": "name",
        "start": "start",
        "tasks": "tasks_count",
    }
    sort_field = sort_fields.get(sort, "name")
    projects_list = projects_list.order_by(sort_field)

    paginator = Paginator(projects_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "projects": page_obj,
        "page_obj": page_obj,
        "search_query": query,
        "sort": sort,
    }
    return render(
        request, "projects_app/project_list.html", context,
    )


def project_detail(request, slug):
    """Карточка проекта по slug."""
    project = get_object_or_404(
        Project.objects.prefetch_related(
            "tasks__researcher", "references"
        ),
        slug=slug,
    )
    context = {
        "project": project,
    }
    return render(
        request, "projects_app/project_detail.html", context,
    )
