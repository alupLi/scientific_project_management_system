from django.http import HttpResponse


BOOTSTRAP_CSS = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/"
    "dist/css/bootstrap.min.css"
)


def page(title: str, content: str) -> str:
    """Собирает HTML-документ с единым каркасом."""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{BOOTSTRAP_CSS}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">Научные проекты</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/projects/">Проекты</a>
                <a class="nav-link" href="/publications/">Публикации</a>
                <a class="nav-link" href="/researchers/">Исследователи</a>
            </div>
        </div>
    </nav>
    <div class="container">
        {content}
    </div>
</body>
</html>"""


def index(request):
    content = """
    <h1 class="display-4">Система управления научными проектами</h1>
    <p class="lead">Приложение для управления научными проектами,
    задачами и публикациями.</p>
    <p>Основные разделы:</p>
    <a href="/projects/" class="btn btn-primary me-2">Проекты</a>
    <a href="/publications/" class="btn btn-secondary me-2">Публикации</a>
    <a href="/researchers/" class="btn btn-outline-secondary">Исследователи</a>
    """
    return HttpResponse(page("Главная", content))


def page_not_found(request, exception):
    """Собственная страница 404."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
