from django.db import models


class Publication(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Название публикации",
    )
    journal = models.CharField(
        max_length=200,
        verbose_name="Журнал",
    )
    date = models.DateField(
        verbose_name="Дата публикации",
    )

    def __str__(self):
        return f"'{self.title}' ({self.date})"

    class Meta:
        ordering = ["-date"]
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
