class Publication:

    def __init__(self, title: str, journal: str, authors: str, date: str):
        self.title = title
        self.journal = journal
        self.authors = authors
        self.date = date

    def __str__(self) -> str:
        return f"'{self.title}' в {self.journal} ({self.date})"

    @classmethod
    def from_dict(cls, data: dict) -> 'Publication':
        return cls(
            title=data["title"],
            journal=data["journal"],
            authors=data["authors"],
            date=data["date"]
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "journal": self.journal,
            "authors": self.authors,
            "date": self.date
        }
