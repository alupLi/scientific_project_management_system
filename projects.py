from typing import List
from datetime import date
from models import Project, Publication


def create_project(projects: List[Project],
                   name: str,
                   start: date,
                   end: date) -> Project:
    new_id = max((p.id for p in projects), default=0) + 1
    new_project = Project(
        new_id, name,
        start.isoformat(), end.isoformat(),
    )
    projects.append(new_project)
    return new_project


def find_projects(projects: List[Project],
                  query: str) -> List[Project]:
    return [p for p in projects if query.lower() in p.name.lower()]


def projects_statistics(projects: List[Project]) -> dict:
    total_tasks = sum(len(p.tasks) for p in projects)
    total_refs = sum(len(p.references) for p in projects)
    return {
        "total_projects": len(projects),
        "total_tasks": total_tasks,
        "total_references": total_refs,
    }


def add_reference_to_project(projects: List[Project],
                             project_id: int,
                             publication: Publication) -> bool:
    """Привязывает публикацию к проекту как источник."""
    project = next((p for p in projects if p.id == project_id), None)
    if not project:
        return False
    project.add_reference(publication)
    return True
