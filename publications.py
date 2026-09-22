from typing import List
from datetime import date
from models import Publication


def add_publication(
    publications: List[Publication],
    title: str,
    journal: str,
    authors: str
) -> Publication:
    new_pub = Publication(title, journal, authors, date.today().isoformat())
    publications.append(new_pub)
    return new_pub


def find_publications(publications: List[Publication],
                      query: str
                      ) -> List[Publication]:
    return [p for p in publications if query.lower() in p.title.lower()]


def publications_by_author(publications: List[Publication],
                           author: str
                           ) -> List[Publication]:
    return [p for p in publications if author.lower() in p.authors.lower()]
