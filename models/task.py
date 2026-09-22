class Task:

    def __init__(self,
                 task_name: str,
                 researcher: str,
                 deadline: str,
                 status: str = "active"):
        self.task_name = task_name
        self.researcher = researcher
        self.deadline = deadline
        self.status = status

    def __str__(self) -> str:
        return (
            f"Задача: {self.task_name} | "
            f"Исполнитель: {self.researcher} | "
            f"Дедлайн: {self.deadline} | "
            f"Статус: {self.status}"
        )

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        return cls(
            task_name=data["task"],
            researcher=data["researcher"],
            deadline=data["deadline"],
            status=data.get("status", "active")
        )

    def to_dict(self) -> dict:
        return {
            "task": self.task_name,
            "researcher": self.researcher,
            "deadline": self.deadline,
            "status": self.status
        }
