import json
from db.database import get_connection


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # 1. Загружаем JSON
    researchers_data = load_json("data/researchers.json")
    pubs_data = load_json("data/publications.json")
    projects_data = load_json("data/projects.json")

    conn = get_connection()
    try:
        # 2. Очищаем таблицы перед импортом
        conn.execute("DELETE FROM project_references")
        conn.execute("DELETE FROM tasks")
        conn.execute("DELETE FROM projects")
        conn.execute("DELETE FROM publications")
        conn.execute("DELETE FROM researchers")

        # 3. Импорт исследователей
        res_rows = [
            (int(rid), data["name"], data["field"])
            for rid, data in researchers_data.items()
        ]
        conn.executemany(
            "INSERT INTO researchers (id, name, field) "
            "VALUES (?, ?, ?)",
            res_rows,
        )

        # 4. Импорт публикаций (собираем ID для связи)
        pub_map = {}  # Словарь: "Название" -> ID в БД
        for pub in pubs_data:
            cur = conn.execute(
                "INSERT INTO publications "
                "(title, journal, date) VALUES (?, ?, ?)",
                (pub["title"], pub["journal"], pub["date"]),
            )
            pub_map[pub["title"]] = cur.lastrowid

        # 5. Импорт проектов и связанных данных
        for pid_str, p_data in projects_data.items():
            pid = int(pid_str)
            # Вставляем проект
            conn.execute(
                "INSERT INTO projects (id, name, start, end) "
                "VALUES (?, ?, ?, ?)",
                (pid, p_data["name"], p_data["start"], p_data["end"]),
            )

            # Вставляем задачи проекта
            for t in p_data.get("tasks", []):
                # Ищем ID исследователя по имени
                res_id = conn.execute(
                    "SELECT id FROM researchers WHERE name = ?",
                    (t["researcher"],),
                ).fetchone()

                if res_id:
                    conn.execute(
                        "INSERT INTO tasks "
                        "(project_id, task_name, researcher_id, "
                        "deadline, status) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (
                            pid,
                            t["task"],
                            res_id["id"],
                            t["deadline"],
                            t.get("status", "active"),
                        ),
                    )

            # Вставляем источники (связь проект-публикация)
            for ref_title in p_data.get("references", []):
                if ref_title in pub_map:
                    conn.execute(
                        "INSERT INTO project_references "
                        "(project_id, publication_id) "
                        "VALUES (?, ?)",
                        (pid, pub_map[ref_title]),
                    )

        conn.commit()
        print("Данные успешно импортированы!")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка при импорте: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
