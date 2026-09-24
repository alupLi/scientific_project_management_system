from typing import List
from .researcher import Researcher


class Publication:

    def __init__(self,
                 title: str,
                 journal: str,
                 authors: List[Researcher],
                 date: str):
        self.title = title
        self.journal = journal
        self.authors = authors
        self.date = date

    def __str__(self) -> str:
        names = ", ".join(r.name for r in self.authors)
        return f"'{self.title}' в {self.journal} ({self.date}) — {names}"

    @classmethod
    def from_dict(cls,
                  data: dict,
                  researchers: list) -> 'Publication':
        authors = []
        for name in data["authors"].split(", "):
            r = next(
                (x for x in researchers if x.name == name.strip()),
                None,
            )
            if r:
                authors.append(r)
        return cls(
            title=data["title"],
            journal=data["journal"],
            authors=authors,
            date=data["date"],
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "journal": self.journal,
            "authors": ", ".join(r.name for r in self.authors),
            "date": self.date,
        }
