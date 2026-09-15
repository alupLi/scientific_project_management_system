from datetime import date

from storage import load_json, save_json
from projects import create_project, find_projects, projects_statistics
from tasks import assign_task
from publications import add_publication
from utils import input_int, input_date

DATA = "data"
PROJECTS_FILE = f"{DATA}/projects.json"
RESEARCHERS_FILE = f"{DATA}/researchers.json"
PUBLICATIONS_FILE = f"{DATA}/publications.json"


# Вывод списка проекта
def show_projects(projects: dict) -> None:
    if not projects:
        print("Проектов нет.")
        return
    for pid, p in projects.items():
        print(
            f"[{pid}] {p['name']} "
            f"({p['start']} — {p['end']}), "
            f"задач: {len(p['tasks'])}"
        )


# Меню приложения
def main() -> None:
    projects = load_json(PROJECTS_FILE, {})
    researchers = load_json(RESEARCHERS_FILE, {})
    publications = load_json(PUBLICATIONS_FILE, [])

    while True:
        print("\n~~~ Система управления научными проектами ~~~")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Назначить задачу")
        print("4. Добавить публикацию")
        print("5. Найти проект")
        print("6. Статистика")
        print("0. Выход")
        choice = input_int("Выберите действие: ")

        if choice == 1:
            show_projects(projects)
        elif choice == 2:
            name = input("Название проекта: ")
            start = input_date("Дата начала (ДД.ММ.ГГГГ): ")
            end = input_date("Дата окончания (ДД.ММ.ГГГГ): ")
            pid = create_project(
                projects,
                name,
                date.fromisoformat(start),
                date.fromisoformat(end),
            )
            print(f"Создан проект id={pid}")
        elif choice == 3:
            pid = input_int("ID проекта: ")
            task = input("Название задачи: ")
            who = input("Исследователь: ")
            deadline = input_date("Дедлайн (ДД.ММ.ГГГГ): ")
            if assign_task(projects, pid, task, who, deadline):
                print("Задача назначена.")
            else:
                print("Проект не найден.")
        elif choice == 4:
            title = input("Название публикации: ")
            journal = input("Журнал: ")
            authors = input("Авторы: ")
            add_publication(publications, title, journal, authors)
            print("Публикация добавлена.")
        elif choice == 5:
            q = input("Поиск по названию: ")
            for p in find_projects(projects, q):
                print(f"[{p['id']}] {p['name']}")
        elif choice == 6:
            print(projects_statistics(projects))
        elif choice == 0:
            break
        else:
            print("Неверный пункт.")

    save_json(PROJECTS_FILE, projects)
    save_json(RESEARCHERS_FILE, researchers)
    save_json(PUBLICATIONS_FILE, publications)
    print("Данные сохранены. Выход.")


if __name__ == "__main__":
    main()
