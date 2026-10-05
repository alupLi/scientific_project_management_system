class Publication:
    """Публикация — внешний источник, изучаемый в проекте."""

    def __init__(self, title: str, journal: str, date: str):
        self.title = title
        self.journal = journal
        self.date = date

    def __str__(self) -> str:
        return f"'{self.title}' — {self.journal} ({self.date})"

    @classmethod
    def from_dict(cls, data: dict) -> 'Publication':
        return cls(
            title=data["title"],
            journal=data["journal"],
            date=data["date"],
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "journal": self.journal,
            "date": self.date,
        }
