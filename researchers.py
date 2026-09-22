from typing import List
from models import Researcher


def add_researcher(researchers: List[Researcher],
                   name: str,
                   field: str
                   ) -> Researcher:
    new_id = max((r.id for r in researchers), default=0) + 1
    new_researcher = Researcher(new_id, name, field)
    researchers.append(new_researcher)
    return new_researcher


def find_researcher(researchers: List[Researcher],
                    query: str
                    ) -> List[Researcher]:
    return [r for r in researchers if query.lower() in r.name.lower()]


def count_researchers(researchers: List[Researcher]) -> int:
    return len(researchers)
