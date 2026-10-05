from datetime import date

from storage import (
    load_projects, save_projects,
    load_researchers, save_researchers,
    load_publications, save_publications,
)
from projects import (
    create_project, find_projects,
    projects_statistics, add_reference_to_project,
)
from tasks import assign_task
from publications import add_publication
from utils import input_int, input_date
from models import Project, Researcher, Publication

DATA = "data"
PROJECTS_FILE = f"{DATA}/projects.json"
RESEARCHERS_FILE = f"{DATA}/researchers.json"
PUBLICATIONS_FILE = f"{DATA}/publications.json"


def show_projects(projects: list[Project]) -> None:
    if not projects:
        print("Проектов нет.")
        return
    for p in projects:
        print(p)


def show_publications(publications: list[Publication]) -> None:
    if not publications:
        print("Публикаций нет.")
        return
    for pub in publications:
        print(pub)


def create_new_project(projects: list[Project]) -> None:
    name = input("Название проекта: ")
    start = input_date("Дата начала (ДД.ММ.ГГГГ): ")
    end = input_date("Дата окончания (ДД.ММ.ГГГГ): ")
    new_project = create_project(
        projects, name,
        date.fromisoformat(start),
        date.fromisoformat(end),
    )
    print(f"Создан проект id={new_project.id}")


def create_new_publication(publications: list[Publication]) -> None:
    title = input("Название публикации: ")
    journal = input("Журнал: ")
    add_publication(publications, title, journal)
    print("Публикация добавлена.")


def link_publication_to_project(
    projects: list[Project],
    publications: list[Publication],
) -> None:
    if not projects:
        print("Проектов нет.")
        return
    if not publications:
        print("Публикаций нет.")
        return

    print("\nДоступные проекты:")
    for p in projects:
        print(p)
    pid = input_int("ID проекта: ")

    print("\nДоступные публикации:")
    for i, pub in enumerate(publications, 1):
        print(f"{i}. {pub}")
    idx = input_int("Номер публикации: ")

    if not (1 <= idx <= len(publications)):
        print("Неверный номер публикации.")
        return

    publication = publications[idx - 1]
    if add_reference_to_project(projects, pid, publication):
        print(f"Публикация '{publication.title}' "
              f"привязана к проекту.")
    else:
        print("Проект не найден.")


def assign_task_to_project(
    projects: list[Project],
    researchers: list[Researcher],
) -> None:
    if not projects:
        print("Проектов нет.")
        return
    if not researchers:
        print("Исследователей нет.")
        return

    pid = input_int("ID проекта: ")
    task_name = input("Название задачи: ")
    who_name = input("Имя исследователя: ")
    who = next(
        (r for r in researchers if r.name == who_name),
        None,
    )
    if not who:
        print("Исследователь не найден.")
        return
    deadline = input_date("Дедлайн (ДД.ММ.ГГГГ): ")
    if assign_task(projects, pid, task_name, who, deadline):
        print("Задача назначена.")
    else:
        print("Проект не найден.")


def main() -> None:
    researchers = load_researchers(RESEARCHERS_FILE)
    publications = load_publications(PUBLICATIONS_FILE)
    projects = load_projects(
        PROJECTS_FILE, researchers, publications,
    )

    while True:
        print("\n~~~ Система управления научными проектами ~~~")
        print("1.  Показать проекты")
        print("2.  Создать проект")
        print("3.  Назначить задачу")
        print("4.  Добавить публикацию")
        print("5.  Показать публикации")
        print("6.  Привязать публикацию к проекту")
        print("7.  Найти проект")
        print("8.  Статистика")
        print("0.  Выход")
        choice = input_int("Выберите действие: ")

        if choice == 1:
            show_projects(projects)
        elif choice == 2:
            create_new_project(projects)
        elif choice == 3:
            assign_task_to_project(projects, researchers)
        elif choice == 4:
            create_new_publication(publications)
        elif choice == 5:
            show_publications(publications)
        elif choice == 6:
            link_publication_to_project(projects, publications)
        elif choice == 7:
            q = input("Поиск по названию: ")
            for p in find_projects(projects, q):
                print(p)
        elif choice == 8:
            print(projects_statistics(projects))
        elif choice == 0:
            break
        else:
            print("Неверный пункт.")

    save_researchers(RESEARCHERS_FILE, researchers)
    save_publications(PUBLICATIONS_FILE, publications)
    save_projects(PROJECTS_FILE, projects)
    print("Данные сохранены. Выход.")


if __name__ == "__main__":
    main()
