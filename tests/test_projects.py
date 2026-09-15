from datetime import date
from projects import create_project, find_projects, projects_statistics


def test_create_project():
    projects = {}
    create_project(projects,
                   "Проект",
                   date(2026, 9, 1),
                   date(2027, 6, 30))
    assert len(projects) == 1


def test_find_projects():
    projects = {}
    create_project(projects,
                   "Проект",
                   date(2026, 9, 1),
                   date(2027, 6, 30))
    assert find_projects(projects, "про")


def test_statistics_empty():
    assert projects_statistics({})["total_projects"] == 0
