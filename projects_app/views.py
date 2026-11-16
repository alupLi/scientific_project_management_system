from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
# from projects_app.models import Project
from django.shortcuts import redirect
from .forms import ProjectForm, TaskForm
from projects_app.models import Project, Task


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


def project_create(request):
    """Создание нового проекта."""
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect(project.get_absolute_url())
    else:
        form = ProjectForm()

    context = {
        "form": form,
        "title": "Создать проект",
    }
    return render(
        request, "projects_app/project_form.html", context,
    )


def project_edit(request, slug):
    """Редактирование существующего проекта."""
    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project,
        )
        if form.is_valid():
            project = form.save()
            return redirect(project.get_absolute_url())
    else:
        form = ProjectForm(instance=project)

    context = {
        "form": form,
        "title": f"Редактировать: {project.name}",
        "project": project,
    }
    return render(
        request, "projects_app/project_form.html", context,
    )


def project_delete(request, slug):
    """Удаление проекта (только POST)."""
    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        project.delete()
        return redirect("projects_app:projects")

    context = {"project": project}
    return render(
        request, "projects_app/project_confirm_delete.html", context,
    )


def task_create(request, slug):
    """Создание задачи для проекта."""
    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = TaskForm(
            request.POST,
            project=project,
        )
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect(project.get_absolute_url())
    else:
        form = TaskForm(project=project)

    context = {
        "form": form,
        "title": f"Добавить задачу в проект: {project.name}",
        "project": project,
    }
    return render(
        request, "projects_app/task_form.html", context,
    )


def task_edit(request, slug, task_id):
    """Редактирование задачи."""
    project = get_object_or_404(Project, slug=slug)
    task = get_object_or_404(Task, pk=task_id, project=project)

    if request.method == "POST":
        form = TaskForm(
            request.POST,
            instance=task,
        )
        if form.is_valid():
            form.save()
            return redirect(project.get_absolute_url())
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
        "title": f"Редактировать задачу: {task.task_name}",
        "project": project,
        "task": task,
    }
    return render(
        request, "projects_app/task_form.html", context,
    )


def task_delete(request, slug, task_id):
    """Удаление задачи (только POST)."""
    project = get_object_or_404(Project, slug=slug)
    task = get_object_or_404(Task, pk=task_id, project=project)

    if request.method == "POST":
        task.delete()
        return redirect(project.get_absolute_url())

    context = {
        "project": project,
        "task": task,
    }
    return render(
        request, "projects_app/task_confirm_delete.html", context,
    )
