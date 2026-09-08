from datetime import date

# Создание проекта
def create_project(name, start, end):
    return {
        "name": name,
        "start": start,
        "end": end,
        "tasks": [],
        "publications": []
    }

# Создание задачи
def assign_task(project, task_name, researcher, deadline):
    project["tasks"].append({
        "task": task_name,
        "researcher": researcher,
        "deadline": deadline,
        "status": "active"
    })
    return f"Задача '{task_name}' назначена {researcher}"

# Добавление публикации
def add_publication(project, title, journal, authors):
    project["publications"].append({
        "title": title,
        "journal": journal,
        "authors": authors,
        "date": date.today()
    })
    return f"Публикация '{title}' добавлена"

# Статус проекта
def check_project_status(project):
    total = len(project["tasks"])
    if total == 0:
        return "Нет задач"
    return f"Всего задач: {total}"

# Текстирование функций
project = create_project("Проект 1", date(2026, 9, 1), date(2027, 6, 30))
print(f"Проект: {project['name']}")

assign_task(project, "Задачча 1", "Чел 1", date(2026, 12, 1))
assign_task(project, "Задача 2", "Чел 2", date(2027, 1, 15))

add_publication(project, "Проект 1", "Публикация 1", "Чел 1, Чел 2")

print(f"Задачи: {len(project['tasks'])}")
print(f"Публикации: {len(project['publications'])}")
print(check_project_status(project))
