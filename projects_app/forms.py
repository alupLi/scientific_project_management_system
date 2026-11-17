from django import forms
from django.core.exceptions import ValidationError
from .models import Project
from .models import Task


class ProjectForm(forms.ModelForm):
    """Форма для создания и редактирования проекта."""

    class Meta:
        model = Project
        fields = (
            "name",
            "start",
            "end",
            "status",
            "references",
            "cover_image",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название проекта",
                }
            ),
            "start": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "end": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-select"},
            ),
            "references": forms.SelectMultiple(
                attrs={"class": "form-select", "size": 5},
            ),
            "cover_image": forms.ClearableFileInput(
                attrs={"class": "form-control"},
            ),
        }
        labels = {
            "name": "Название",
            "start": "Дата начала",
            "end": "Дата окончания",
            "status": "Статус",
            "references": "Изученные источники",
            "cover_image": "Обложка",
        }

    def clean(self):
        """Проверка, что дата окончания не раньше даты начала."""
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")

        if start and end and end < start:
            raise ValidationError(
                "Дата окончания не может быть раньше даты начала."
            )
        return cleaned_data


class TaskForm(forms.ModelForm):
    """Форма для создания и редактирования задачи."""

    class Meta:
        model = Task
        fields = (
            "task_name",
            "researcher",
            "deadline",
            "status",
        )
        widgets = {
            "task_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название задачи",
                }
            ),
            "researcher": forms.Select(
                attrs={"class": "form-select"},
            ),
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-select"},
            ),
        }
        labels = {
            "task_name": "Название задачи",
            "researcher": "Исполнитель",
            "deadline": "Дедлайн",
            "status": "Статус",
        }

    def __init__(self, *args, project=None, **kwargs):
        """Сохраняем проект, чтобы использовать его в валидации."""
        super().__init__(*args, **kwargs)
        self.project = project

    def clean(self):
        """Проверка дедлайна и уникальности названия задачи в проекте."""
        cleaned_data = super().clean()
        deadline = cleaned_data.get("deadline")
        task_name = cleaned_data.get("task_name")

        # Проект берем либо переданный, либо из редактируемой задачи
        project = self.project or (
            self.instance.project if self.instance.pk else None
        )

        # Проверка даты
        if project and deadline and deadline < project.start:
            raise ValidationError(
                "Дедлайн не может быть раньше даты начала проекта "
                f"({project.start})."
            )

        # Проверка уникальности названия задачи в рамках проекта
        if project and task_name:
            # Ищем задачи с таким же названием в этом проекте
            conflicts = Task.objects.filter(
                project=project,
                task_name__iexact=task_name,
            )

            # При редактировании исключаем текущую задачу
            if self.instance.pk:
                conflicts = conflicts.exclude(pk=self.instance.pk)

            if conflicts.exists():
                raise ValidationError(
                    f"В проекте «{project.name}» уже есть задача "
                    f"с названием «{task_name}»."
                )

        return cleaned_data
