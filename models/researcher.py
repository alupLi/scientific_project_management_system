class Researcher:

    def __init__(self, researcher_id: int, name: str, field: str):
        self.id = researcher_id
        self.name = name
        self.field = field

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} ({self.field})"

    @classmethod
    def from_dict(cls, data: dict) -> 'Researcher':
        return cls(
            researcher_id=data["id"],
            name=data["name"],
            field=data["field"]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "field": self.field
        }
