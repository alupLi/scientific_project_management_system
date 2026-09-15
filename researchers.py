# Добавление исследователя
def add_researcher(researchers: dict, name: str, field: str) -> int:
    new_id = max(researchers.keys(), default=0) + 1
    researchers[new_id] = {"name": name, "field": field}
    return new_id


# Поиск исследователя по имени
def find_researcher(researchers: dict, query: str) -> list:
    return [
        {"id": rid, **data}
        for rid, data in researchers.items()
        if query.lower() in data["name"].lower()
    ]


# Количество исследователей
def count_researchers(researchers: dict) -> int:
    return len(researchers)
