from .models import Project


def project_context(request):
    """Передает общие данные о проектах в шаблоны."""
    return {
        "site_name": "Управление научными проектами",
        "projects_count": Project.objects.count(),
    }
