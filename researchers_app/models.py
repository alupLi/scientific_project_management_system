from django.db import models


class Researcher(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Имя исследователя",
    )
    field = models.CharField(
        max_length=200,
        verbose_name="Область исследований",
    )

    def __str__(self):
        return f"{self.name} ({self.field})"

    class Meta:
        ordering = ["name"]
        verbose_name = "Исследователь"
        verbose_name_plural = "Исследователи"
