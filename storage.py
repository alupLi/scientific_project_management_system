import json
import os
from typing import List, Any, TypeVar
from models import Project, Researcher, Publication

T = TypeVar('T')


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


def load_projects(filename: str) -> List[Project]:
    raw_data = load_json(filename, {})
    projects = []
    for pid, p_data in raw_data.items():
        projects.append(Project.from_dict(int(pid), p_data))
    return projects


def load_researchers(filename: str) -> List[Researcher]:
    raw_data = load_json(filename, {})
    researchers = []
    for rid, r_data in raw_data.items():
        r_data['id'] = int(rid)
        researchers.append(Researcher.from_dict(r_data))
    return researchers


def load_publications(filename: str) -> List[Publication]:
    raw_data = load_json(filename, [])
    return [Publication.from_dict(p) for p in raw_data]


def save_projects(filename: str, projects: List[Project]) -> None:
    data_to_save = {str(p.id): p.to_dict() for p in projects}
    save_json(filename, data_to_save)


def save_researchers(filename: str, researchers: List[Researcher]) -> None:
    data_to_save = {
        str(r.id): {"name": r.name, "field": r.field}
        for r in researchers
    }
    save_json(filename, data_to_save)


def save_publications(filename: str, publications: List[Publication]) -> None:
    data_to_save = [p.to_dict() for p in publications]
    save_json(filename, data_to_save)
