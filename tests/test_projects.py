from datetime import date
from projects import (
    create_project, find_projects,
    projects_statistics, add_reference_to_project,
)
from models import Project, Publication


def test_create_project():
    projects = []
    create_project(
        projects, "Проект",
        date(2026, 9, 1), date(2027, 6, 30),
    )
    assert len(projects) == 1
    assert isinstance(projects[0], Project)


def test_find_projects():
    projects = []
    create_project(
        projects, "Проект",
        date(2026, 9, 1), date(2027, 6, 30),
    )
    assert find_projects(projects, "про")


def test_statistics_empty():
    assert projects_statistics([])["total_projects"] == 0


def test_add_reference_to_project():
    projects = []
    p = create_project(
        projects, "Проект",
        date(2026, 9, 1), date(2027, 6, 30),
    )
    pub = Publication("Публикация", "Журнал", "2026-09-15")
    assert add_reference_to_project(projects, p.id, pub)
    assert len(projects[0].references) == 1
    assert projects[0].references[0] is pub
