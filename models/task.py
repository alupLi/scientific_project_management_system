from .researcher import Researcher


class Task:

    def __init__(self,
                 task_name: str,
                 researcher: Researcher,
                 deadline: str,
                 status: str = "active"):
        self.task_name = task_name
        self.researcher = researcher
        self.deadline = deadline
        self.status = status

    def __str__(self) -> str:
        return (
            f"Задача: {self.task_name} | "
            f"Исполнитель: {self.researcher.name} | "
            f"Дедлайн: {self.deadline} | "
            f"Статус: {self.status}"
        )

    @classmethod
    def from_dict(cls,
                  data: dict,
                  researchers: list) -> 'Task':
        researcher = next(
            (r for r in researchers if r.name == data["researcher"]),
            None,
        )
        return cls(
            task_name=data["task"],
            researcher=researcher,
            deadline=data["deadline"],
            status=data.get("status", "active"),
        )

    def to_dict(self) -> dict:
        return {
            "task": self.task_name,
            "researcher": self.researcher.name if self.researcher else "",
            "deadline": self.deadline,
            "status": self.status,
        }
