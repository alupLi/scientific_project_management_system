# Система управления научными проектами

---

## Назначение

Приложение для управления научными проектами. 
Оно позволяет исследователям и руководителям планировать этапы работы, 
отслеживать прогресс задач и управлять результатами интеллектуальной деятельности.

## Целевая аудитория

- Научные сотрудники и исследователи
- Руководители лабораторий и научных групп
- Администраторы научных фондов и грантов

## Описание предметной области

Управление жизненным циклом научного проекта, который включает в себя планирование задач, распределение ресурсов и контроль сроков.

---

## Основные сущности

- исследователь
- проект
- задача
- публикация

## Основные функции

- Создание и управление профилями исследователей.
- Создание научных проектов с указанием сроков.
- Назначение задач исследователям и отслеживание их статуса.
- Учет публикаций и их привязка к проектам и авторам.

---

## План развития проекта

- Разработка веб-приложения с использованием фреймворка Django.
- Подключение базы данных (PostgreSQL) для хранения информации.
- Реализация системы аутентификации и авторизации пользователей.
- Разработка REST API для интеграции с другими системами.
- Контейнеризация приложения с использованием Docker.
- Настройка CI/CD для автоматического тестирования и развертывания.

---

## Возможности
- создание проектов с указанием сроков;
- назначение задач исследователям;
- учёт публикаций и их привязка к проектам;
- поиск проектов и публикаций;
- статистика по проектам;
- сохранение данных в JSON-файлах.

## Структура проекта
```
room_booking/
├── manage.py
├── roomly/                  # настройки Django-проекта
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── homepage/                # главная страница
│   ├── views.py             # page() — общий каркас HTML, index()
│   └── urls.py
├── projects_app/            # приложение проектов
│   ├── views.py             # projects(), project_detail()
│   └── urls.py
├── publications_app/        # приложение публикаций
│   ├── views.py             # publications()
│   └── urls.py
├── researchers_app/         # приложение исследователей
│   ├── views.py             # researchers()
│   └── urls.py
├── models/                  # классы предметной области (ПР3)
│   ├── __init__.py
│   ├── project.py
│   ├── task.py
│   ├── researcher.py
│   └── publication.py
├── data/                    # JSON-хранилище
│   ├── projects.json
│   ├── publications.json
│   └── researchers.json
├── tests/                   # тесты ПР3
├── main.py                  # консольная версия (сохранена)
├── storage.py
├── utils.py
├── projects.py
├── tasks.py
├── publications.py
├── researchers.py
├── requirements.txt
└── README.md
```

## Основные классы

### Researcher
- **Атрибуты**: `id`, `name`, `field`.
- **Методы**: `__str__`, `from_dict`, `to_dict`.

### Project
- **Атрибуты**: `id`, `name`, `start`, `end`, `tasks` (список объектов Task).
- **Методы**: `add_task`, `__str__`, `from_dict`, `to_dict`.

### Task
- **Атрибуты**: `task_name`, `researcher`, `deadline`, `status`.
- **Методы**: `__str__`, `from_dict`, `to_dict`.

### Publication
- **Атрибуты**: `title`, `journal`, `authors`, `date`.
- **Методы**: `__str__`, `from_dict`, `to_dict`.

## Используемые технологии

* Python 3
* Django 5.2 — веб-фреймворк
* HTML — разметка веб-страниц
* CSS и Bootstrap 5.3 — оформление страниц
* pytest — автоматизированные тесты
* flake8 — проверка качества кода

## Веб-интерфейс

Веб-часть приложения реализована на Django 5.2 с использованием
системы шаблонов Django.

### Страницы

| URL | Назначение | Шаблон |
|-----|-----------|--------|
| `/` | Главная | `homepage/index.html` |
| `/projects/` | Список проектов | `projects_app/project_list.html` |
| `/projects/<int:project_id>/` | Карточка проекта | `projects_app/project_detail.html` |
| `/publications/` | Список публикаций | `publications_app/publication_list.html` |
| `/researchers/` | Список исследователей | `researchers_app/researcher_list.html` |

### Шаблоны

- `templates/base.html` — базовый шаблон с блоками `{% block title %}` и `{% block content %}`
- `templates/includes/navigation.html` — общая навигация (подключается через `{% include %}`)
- `projects_app/templates/projects_app/includes/project_card.html` — карточка проекта
- Шаблоны приложений наследуют `base.html` через `{% extends %}`

### Статические файлы

Расположены в `homepage/static/homepage/`:
- `css/style.css` — собственные стили
- `js/main.js` — вывод текущего года в подвале
- `img/logo.png` — логотип


## Хранение данных (ПР7)

Проект использует двухуровневую систему хранения:
1. **SQLite-база данных** — основное хранилище для веб-интерфейса.
2. **JSON-файлы** — исходные данные, сохранённые с предыдущих этапов.

### Структура базы данных

Файл базы данных: `data/project_db.sqlite`.

Таблицы:
- `researchers` (id, name, field) — исследователи;
- `publications` (id, title, journal, date) — публикации;
- `projects` (id, name, start, end) — научные проекты;
- `tasks` (id, project_id, task_name, researcher_id, deadline, status) — задачи;
- `project_references` (project_id, publication_id) — связь проектов и публикаций (многие ко многим).

Внешние ключи:
- `tasks.project_id` → `projects.id`
- `tasks.researcher_id` → `researchers.id`
- `project_references.project_id` → `projects.id`
- `project_references.publication_id` → `publications.id`

### Модули работы с базой данных

- `sql/schema.sql` — SQL-команды создания таблиц;
- `sql/queries.sql` — все разработанные SQL-запросы (выборка, фильтрация, JOIN, COUNT, GROUP BY);
- `db/database.py` — подключение к SQLite с включением проверки внешних ключей и настройкой `row_factory`;
- `db/queries.py` — функции получения данных для Django-представлений;
- `db/import_json.py` — скрипт переноса данных из JSON в SQLite.

## Слой данных (ПР9)

Начиная с ПР9, проект использует **Django ORM** для работы с базой данных. 
Ручные SQL-запросы (из ПР7) больше не используются в представлениях.

### Модели
- **Researcher** (`researchers_app`): `name`, `field`
- **Publication** (`publications_app`): `title`, `journal`, `date`
- **Project** (`projects_app`): `name`, `start`, `end`, `references` (M2M с Publication)
- **Task** (`projects_app`): `project` (FK), `researcher` (FK), `task_name`, `deadline`, `status`

### Миграции
Для управления структурой БД используются миграции Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Перенос данных
Данные из базы ПР7 перенесены в базу Django (`db.sqlite3`) с помощью скрипта `db/import_to_orm.py`.

### Работа с данными
- Списки, фильтрация, сортировка и пагинация реализованы через методы ORM (`all()`, `filter()`, `order_by()`, `annotate()`, `Paginator`).
- Карточки объектов используют `get_object_or_404()` и связанные модели (через `select_related` и `prefetch_related`).

### Архитектура

HTML больше не формируется в Python-коде. Функция `page()` из ПР5 удалена.
Все ссылки формируются через `{% url %}` с использованием namespace приложений.

---

## Запуск

### Требования
- Python 3.x
- pytest
- flake8
- Django==5.2.* Для веб версии

`py -m pip install -r requirements.txt`

### Пересоздание базы данных

Если база данных повреждена или требуется пересоздать её из JSON:

```bash
# 1. Удалить старый файл базы
Remove-Item .\data\project_db.sqlite

# 2. Создать пустой файл
py -c "import sqlite3; sqlite3.connect('data/project_db.sqlite').close()"

# 3. Применить схему
py -c "import sqlite3; conn=sqlite3.connect('data/project_db.sqlite'); conn.executescript(open('sql/schema.sql', encoding='utf-8').read()); conn.close()"

# 4. Импортировать данные из JSON
py -m db.import_json

### Веб-версия (Django)

```bash
venv\Scripts\activate
py manage.py runserver
```

Затем открыть в браузере: http://127.0.0.1:8000/

### Консольная версия
py -m main.py

### Тесты
py -m pytest

### Проверка
py -m flake8

---

## Текущее состояние

Реализовано:
- ПР1–ПР3: консольное приложение с ООП-моделью и JSON-хранилищем;
- ПР5: Django-проект и веб-страницы (HTTP, URL, views);
- ПР6: Django-шаблоны (base.html, extends, include, static);
- ПР7: база данных SQLite, SQL-запросы, перенос данных из JSON.
