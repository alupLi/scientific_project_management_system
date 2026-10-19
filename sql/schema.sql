-- Схема базы данных проекта

CREATE TABLE IF NOT EXISTS researchers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    field TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS publications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    journal TEXT NOT NULL,
    date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start TEXT NOT NULL,
    end TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    task_name TEXT NOT NULL,
    researcher_id INTEGER NOT NULL,
    deadline TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (researcher_id) REFERENCES researchers(id)
);

CREATE TABLE IF NOT EXISTS project_references (
    project_id INTEGER NOT NULL,
    publication_id INTEGER NOT NULL,
    PRIMARY KEY (project_id, publication_id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (publication_id) REFERENCES publications(id)
);