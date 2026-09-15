# Добавление задачи в проет
def assign_task(
    projects: dict,
    project_id: int,
    task_name: str,
    researcher: str,
    deadline: str,
) -> bool:
    if project_id not in projects:
        return False
    projects[project_id]["tasks"].append({
        "task": task_name,
        "researcher": researcher,
        "deadline": deadline,
        "status": "active",
    })
    return True


# Статус задачи
def get_task_status(is_active: bool) -> str:
    if is_active:
        return "Задача активна"
    return "Задача завершена"


# Фильтр задач по статусу
def filter_tasks_by_status(projects: dict, status: str) -> list:
    for project in projects.values():
        for task in project["tasks"]:
            if task["status"] == status:
                task
