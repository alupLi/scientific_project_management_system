from datetime import date

# Создание проекта
def create_project(name, start, end):
    return {
        "name": name,
        "start": start,
        "end": end,
        "tasks": []
    }

# Назначение задач
def assign_task(project, task_name, researcher):
    project["tasks"].append({
        "task": task_name,
        "researcher": researcher,
        "status": "active"
    })
    return f"Задача '{task_name}' назначена {researcher}"

# Привязка публикаций к проектам
def add_publication(title, project_name, authors):
    return f"Публикация '{title}' добавлена к проекту '{project_name}'"

# Тестирование функций
project = create_project("Квантовые вычисления", date(2026, 9, 1), date(2027, 6, 30))
print(f"Проект: {project['name']}")
print(assign_task(project, "Разработка алгоритма", "Иванов И.И."))
print(add_publication("Квантовые алгоритмы", project['name'], "Иванов И.И., Петров П.П."))
print(f"Задачи в проекте: {len(project['tasks'])}")