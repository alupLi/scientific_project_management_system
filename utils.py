from datetime import datetime


# Валидация целого числа
def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


# Вализация даты
def input_date(prompt: str) -> str:
    while True:
        raw = input(prompt)
        try:
            return datetime.strptime(raw, "%d.%m.%Y").date().isoformat()
        except ValueError:
            print("Ошибка: формат даты ДД.ММ.ГГГГ.")
