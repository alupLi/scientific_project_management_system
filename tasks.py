from typing import List
from models import Project, Task


# Назначение задачи проекту
def assign_task(
    projects: List[Project],
    project_id: int,
    task_name: str,
    researcher: str,
    deadline: str,
) -> bool:
    project = next((p for p in projects if p.id == project_id), None)
    if not project:
        return False

    new_task = Task(task_name, researcher, deadline)
    project.add_task(new_task)
    return True


def get_task_status(is_active: bool) -> str:
    if is_active:
        return "Задача активна"
    return "Задача завершена"


# Фильтр задачи по статусу
def filter_tasks_by_status(projects: List[Project], status: str) -> List[Task]:
    result = []
    for project in projects:
        for task in project.tasks:
            if task.status == status:
                result.append(task)
    return result
