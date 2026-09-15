from datetime import date


# Добавление публикации
def add_publication(publications: list, title: str, journal: str, authors: str
                    ) -> dict:
    pub = {
        "title": title,
        "journal": journal,
        "authors": authors,
        "date": date.today().isoformat(),
    }
    publications.append(pub)
    return pub


# Поиск публикации по названию
def find_publications(publications: list, query: str) -> list:
    return [p for p in publications if query.lower() in p["title"].lower()]


# Публикации определенного автора
def publications_by_author(publications: list, author: str) -> list:
    return [p for p in publications if author.lower() in p["authors"].lower()]
