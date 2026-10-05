import json
import os
from typing import List, Any

from models import Project, Researcher, Publication


def load_json(filename: str, default: Any) -> Any:
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(filename: str, data: Any) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_researchers(filename: str) -> List[Researcher]:
    raw = load_json(filename, {})
    return [
        Researcher.from_dict({**data, "id": int(rid)})
        for rid, data in raw.items()
    ]


def save_researchers(filename: str,
                     researchers: List[Researcher]) -> None:
    data = {
        str(r.id): {"name": r.name, "field": r.field}
        for r in researchers
    }
    save_json(filename, data)


def load_publications(filename: str) -> List[Publication]:
    raw = load_json(filename, [])
    return [Publication.from_dict(p) for p in raw]


def save_publications(filename: str,
                      publications: List[Publication]) -> None:
    save_json(filename, [p.to_dict() for p in publications])


def load_projects(filename: str,
                  researchers: List[Researcher],
                  publications: List[Publication]) -> List[Project]:
    raw = load_json(filename, {})
    projects = []
    for pid, p_data in raw.items():
        projects.append(
            Project.from_dict(
                int(pid), p_data, researchers, publications,
            )
        )
    return projects


def save_projects(filename: str, projects: List[Project]) -> None:
    data = {str(p.id): p.to_dict() for p in projects}
    save_json(filename, data)
