from db.database import get_connection


def get_all_projects():
    """Возвращает список всех проектов с подсчетом задач и источников."""
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT
            p.id,
            p.name,
            p.start,
            p.end,
            COUNT(DISTINCT t.id) AS tasks_count,
            COUNT(DISTINCT pr.publication_id) AS refs_count
        FROM projects p
        LEFT JOIN tasks t ON p.id = t.project_id
        LEFT JOIN project_references pr ON p.id = pr.project_id
        GROUP BY p.id, p.name, p.start, p.end
        ORDER BY p.name
        """
    ).fetchall()
    conn.close()
    return rows


def get_project_by_id(project_id):
    """Возвращает один проект по ID."""
    conn = get_connection()
    row = conn.execute(
        "SELECT id, name, start, end FROM projects WHERE id = ?",
        (project_id,),
    ).fetchone()
    conn.close()
    return row


def get_tasks_for_project(project_id):
    """Возвращает задачи конкретного проекта с именами исполнителей."""
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT t.id, t.task_name, r.name AS researcher_name,
               t.deadline, t.status
        FROM tasks t
        JOIN researchers r ON t.researcher_id = r.id
        WHERE t.project_id = ?
        ORDER BY t.deadline
        """,
        (project_id,),
    ).fetchall()
    conn.close()
    return rows


def get_publications_for_project(project_id):
    """Возвращает источники (публикации) конкретного проекта."""
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT pub.id, pub.title, pub.journal, pub.date
        FROM project_references pr
        JOIN publications pub ON pr.publication_id = pub.id
        WHERE pr.project_id = ?
        ORDER BY pub.date DESC
        """,
        (project_id,),
    ).fetchall()
    conn.close()
    return rows


def get_all_publications():
    """Возвращает список всех публикаций."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, title, journal, date "
        "FROM publications ORDER BY date DESC"
    ).fetchall()
    conn.close()
    return rows


def get_all_researchers():
    """Возвращает список всех исследователей."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name, field FROM researchers ORDER BY name"
    ).fetchall()
    conn.close()
    return rows


def search_projects(query):
    """Ищет проекты по вхождению подстроки в название."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name FROM projects WHERE name LIKE ?",
        (f"%{query}%",),
    ).fetchall()
    conn.close()
    return rows


def get_researcher_stats():
    """Статистика: сколько задач у каждого исследователя."""
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT r.name AS researcher_name,
               COUNT(t.id) AS task_count
        FROM researchers r
        LEFT JOIN tasks t ON r.id = t.researcher_id
        GROUP BY r.id, r.name
        ORDER BY task_count DESC
        """
    ).fetchall()
    conn.close()
    return rows
