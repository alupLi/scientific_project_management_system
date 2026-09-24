from typing import List
from datetime import date
from models import Publication, Researcher


def add_publication(
    publications: List[Publication],
    title: str,
    journal: str,
    authors: List[Researcher],
) -> Publication:
    new_pub = Publication(
        title, journal, authors, date.today().isoformat()
    )
    publications.append(new_pub)
    return new_pub


def find_publications(
    publications: List[Publication], query: str
) -> List[Publication]:
    return [
        p for p in publications
        if query.lower() in p.title.lower()
    ]


def publications_by_author(
    publications: List[Publication], author: str
) -> List[Publication]:
    query = author.lower()
    return [
        p for p in publications
        if any(query in r.name.lower() for r in p.authors)
    ]
