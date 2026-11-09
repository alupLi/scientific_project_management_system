from django.db import models
from django.urls import reverse  # <-- Обязательно добавь этот импорт!
from django.utils.text import slugify
from unidecode import unidecode
# Импортируем модели из других приложений для связей
from researchers_app.models import Researcher
from publications_app.models import Publication


class Project(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Активен"
        COMPLETED = "completed", "Завершен"
        CANCELLED = "cancelled", "Отменен"

    name = models.CharField(
        max_length=300,
        verbose_name="Название проекта",
    )
    start = models.DateField(
        verbose_name="Дата начала",
    )
    end = models.DateField(
        verbose_name="Дата окончания",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        verbose_name="Статус проекта",
    )
    slug = models.SlugField(
        max_length=300,
        unique=True,
        blank=True,
        verbose_name="URL-идентификатор",
    )
    references = models.ManyToManyField(
        Publication,
        blank=True,
        related_name="projects",
        verbose_name="Изученные источники",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(unidecode(self.name)) or "project"
            # Если проект новый, pk еще нет
            if not self.pk:
                super().save(*args, **kwargs)
                base = slugify(unidecode(self.name)) or "project"
                self.slug = f"{base}-{self.pk}"
                super().save(update_fields=["slug"])
                return
            self.slug = f"{base}-{self.pk}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    # Вот этот метод нужно добавить:
    def get_absolute_url(self):
        """Возвращает URL карточки проекта."""
        return reverse(
            "projects_app:project_detail",
            kwargs={"slug": self.slug},
        )

    class Meta:
        ordering = ["name"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class TaskQuerySet(models.QuerySet):
    """Набор запросов для задач."""
    def active(self):
        return self.filter(status=Task.Status.ACTIVE)

    def completed(self):
        return self.filter(status=Task.Status.COMPLETED)

    def cancelled(self):
        return self.filter(status=Task.Status.CANCELLED)


class TaskManager(models.Manager.from_queryset(TaskQuerySet)):
    """Менеджер модели Task."""
    pass


class Task(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Активна"
        COMPLETED = "completed", "Завершена"
        CANCELLED = "cancelled", "Отменена"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", verbose_name="Проект")
    researcher = models.ForeignKey(Researcher, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks", verbose_name="Исполнитель")
    task_name = models.CharField(max_length=300, verbose_name="Название задачи", help_text="Введите название задачи")
    deadline = models.DateField(verbose_name="Дедлайн")
    status = models.CharField(
        max_length=50, 
        choices=Status.choices, 
        default=Status.ACTIVE, 
        verbose_name="Статус"
    )
    
    objects = TaskManager()

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ["deadline"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
