from typing import List
from .task import Task


class Project:

    def __init__(self,
                 project_id: int,
                 name: str,
                 start: str,
                 end: str,
                 tasks: List[Task] = None):
        self.id = project_id
        self.name = name
        self.start = start
        self.end = end
        self.tasks = tasks if tasks is not None else []

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.name} "
            f"({self.start} — {self.end}), "
            f"задач: {len(self.tasks)}"
        )

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    @classmethod
    def from_dict(cls,
                  project_id: int,
                  data: dict,
                  researchers: list) -> 'Project':
        tasks_data = data.get("tasks", [])
        tasks = [Task.from_dict(t, researchers) for t in tasks_data]
        return cls(
            project_id=project_id,
            name=data["name"],
            start=data["start"],
            end=data["end"],
            tasks=tasks,
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "start": self.start,
            "end": self.end,
            "tasks": [t.to_dict() for t in self.tasks],
        }
