-- 1. ВЫБОРКА СПИСКОВ (SELECT)

-- 1.1. Список всех проектов с сортировкой по названию
SELECT id, name, start, end 
FROM projects 
ORDER BY name;

-- 1.2. Список всех публикаций с сортировкой по дате (сначала новые)
SELECT id, title, journal, date 
FROM publications 
ORDER BY date DESC;



-- 2. ФИЛЬТРАЦИЯ (WHERE)

-- 2.1. Поиск проектов по части названия (параметр передается из Django)
SELECT id, name 
FROM projects 
WHERE name LIKE '%исследование%';

-- 2.2. Поиск активных задач (статус 'active')
SELECT id, task_name, deadline 
FROM tasks 
WHERE status = 'active';



-- 3. СОЕДИНЕНИЕ ТАБЛИЦ (JOIN)

-- 3.1. Полная информация о задачах (задача + название проекта + имя исследователя)
SELECT 
    t.id, 
    t.task_name, 
    p.name AS project_name, 
    r.name AS researcher_name, 
    t.deadline, 
    t.status
FROM tasks t
JOIN projects p ON t.project_id = p.id
JOIN researchers r ON t.researcher_id = r.id
ORDER BY t.deadline;

-- 3.2. Список источников (публикаций) для конкретного проекта
SELECT 
    p.name AS project_name, 
    pub.title AS publication_title, 
    pub.journal, 
    pub.date
FROM project_references pr
JOIN projects p ON pr.project_id = p.id
JOIN publications pub ON pr.publication_id = pub.id
WHERE p.id = 1;



-- 4. АГРЕГАТНЫЕ ФУНКЦИИ (COUNT, MIN, MAX)

-- 4.1. Общее количество проектов в базе
SELECT COUNT(*) AS total_projects 
FROM projects;

-- 4.2. Количество задач со статусом 'active'
SELECT COUNT(*) AS active_tasks_count 
FROM tasks 
WHERE status = 'active';



-- 5. ГРУППИРОВКА (GROUP BY, HAVING)

-- 5.1. Количество задач у каждого исследователя
-- (Страница статистики)
SELECT 
    r.name AS researcher_name, 
    COUNT(t.id) AS task_count
FROM researchers r
LEFT JOIN tasks t ON r.id = t.researcher_id
GROUP BY r.id, r.name
ORDER BY task_count DESC;

-- 5.2. Проекты, у которых более 1 источника (публикации)
-- (Демонстрация HAVING)
SELECT 
    p.name AS project_name, 
    COUNT(pr.publication_id) AS refs_count
FROM projects p
JOIN project_references pr ON p.id = pr.project_id
GROUP BY p.id, p.name
HAVING COUNT(pr.publication_id) > 1;
