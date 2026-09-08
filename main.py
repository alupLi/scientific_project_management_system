from datetime import date

# тестовые данные
project = "Проект 1"
task = "Задача 1"
deadline = date(2026, 9, 25)

# функция для вывода оставшихся дней
def check_deadline(deadline):
    days = (deadline - date.today()).days
    if days < 0:
        return "Просрочено!"
    else:
        return f"{days} дней осталось."

# тестовый вывод
print(f"Проект: {project}")
print(f"Задача: {task}")
print(f"Дедлайн: {deadline}")
print(check_deadline(deadline))