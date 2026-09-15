from datetime import date


# Создать проетк
def create_project(projects: dict, name: str, start: date, end: date) -> int:
    new_id = max(projects.keys(), default=0) + 1
    projects[new_id] = {
        "name": name,
        "start": start.isoformat(),
        "end": end.isoformat(),
        "tasks": [],
    }
    return new_id


# Поиск проекта по названию
def find_projects(projects: dict, query: str) -> list:
    return [
        {"id": pid, **data}
        for pid, data in projects.items()
        if query.lower() in data["name"].lower()
    ]


# Сортировка проектов по названию
def sort_projects_by_name(projects: dict) -> list:
    return sorted(projects.items(), key=lambda item: item[1]["name"])


# Статискика проекта
def projects_statistics(projects: dict) -> dict:
    total_tasks = sum(len(p["tasks"]) for p in projects.values())
    return {"total_projects": len(projects), "total_tasks": total_tasks}
