from datetime import date
from projects import create_project
from tasks import assign_task, get_task_status


def test_assign_task():
    projects = []
    new_project = create_project(
        projects,
        "Проект",
        date(2026, 9, 1),
        date(2027, 1, 1),
    )
    assert assign_task(
        projects,
        new_project.id,
        "Задача",
        "Исследователь",
        "2026-12-01",
    )
    assert len(projects[0].tasks) == 1


def test_assign_to_missing_project():
    assert not assign_task([], 99, "Задача", "Исследователь", "2026-12-01")


def test_get_task_status():
    assert get_task_status(True) == "Задача активна"
