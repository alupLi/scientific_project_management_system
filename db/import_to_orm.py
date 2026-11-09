import os
import sys
import sqlite3
import django
from datetime import date
from pathlib import Path
from researchers_app.models import Researcher
from publications_app.models import Publication
from projects_app.models import Project, Task

# Настраиваем Django
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roomly.settings")
django.setup()

# Настраиваем Django
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roomly.settings")
django.setup()


SOURCE_DB = BASE_DIR / "data" / "project_db.sqlite"


def main():
    if not SOURCE_DB.exists():
        print("Исходная база не найдена!")
        return

    print("Начинаем перенос из SQLite ПР7...")

    conn = sqlite3.connect(SOURCE_DB)
    conn.row_factory = sqlite3.Row

    # 1. Перенос исследователей
    researchers = conn.execute("SELECT * FROM researchers").fetchall()
    for row in researchers:
        Researcher.objects.update_or_create(
            id=row["id"],
            defaults={"name": row["name"], "field": row["field"]}
        )

    # 2. Перенос публикаций
    pub_map = {}
    pubs = conn.execute("SELECT * FROM publications").fetchall()
    for row in pubs:
        obj, _ = Publication.objects.update_or_create(
            id=row["id"],
            defaults={
                "title": row["title"],
                "journal": row["journal"],
                "date": date.fromisoformat(row["date"]),
            }
        )
        pub_map[row["id"]] = obj

    # 3. Перенос проектов и задач
    projects = conn.execute("SELECT * FROM projects").fetchall()
    for row in projects:
        project = Project.objects.update_or_create(
            id=row["id"],
            defaults={
                "name": row["name"],
                "start": date.fromisoformat(row["start"]),
                "end": date.fromisoformat(row["end"]),
            }
        )[0]

        # Восстанавливаем связи с публикациями (таблица project_references)
        refs = conn.execute(
            "SELECT publication_id "
            "FROM project_references "
            "WHERE project_id = ?",
            (row["id"],)
        ).fetchall()
        for ref in refs:
            if ref["publication_id"] in pub_map:
                project.references.add(pub_map[ref["publication_id"]])

    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    for row in tasks:
        Task.objects.update_or_create(
            id=row["id"],
            defaults={
                "project_id": row["project_id"],
                "task_name": row["task_name"],
                "researcher_id": row["researcher_id"],
                "deadline": date.fromisoformat(row["deadline"]),
                "status": row["status"],
            }
        )

    conn.close()
    print("Перенос успешно завершен!")


if __name__ == "__main__":
    main()
