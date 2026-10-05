from typing import List
from datetime import date
from models import Publication


def add_publication(publications: List[Publication],
                    title: str,
                    journal: str) -> Publication:
    new_pub = Publication(
        title, journal, date.today().isoformat(),
    )
    publications.append(new_pub)
    return new_pub


def find_publications(publications: List[Publication],
                      query: str) -> List[Publication]:
    return [
        p for p in publications
        if query.lower() in p.title.lower()
    ]
