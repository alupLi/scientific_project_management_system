from django.db import models

# Импортируем модели из других приложений для связей
from researchers_app.models import Researcher
from publications_app.models import Publication


class Project(models.Model):
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
    # Связь "многие ко многим": проект изучает несколько публикаций
    references = models.ManyToManyField(
        Publication,
        blank=True,
        related_name="projects",
        verbose_name="Изученные источники",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Task(models.Model):
    # Связь "многие к одному": в проекте много задач
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Проект",
    )
    # Связь "многие к одному": исполнитель задачи
    researcher = models.ForeignKey(
        Researcher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Исполнитель",
    )
    task_name = models.CharField(
        max_length=300,
        verbose_name="Название задачи",
    )
    deadline = models.DateField(
        verbose_name="Дедлайн",
    )
    status = models.CharField(
        max_length=50,
        default="active",
        verbose_name="Статус",
    )

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ["deadline"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
