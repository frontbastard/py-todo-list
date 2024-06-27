from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(
        verbose_name="Task Description"
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Optional deadline for the task",
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Completed"
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="tasks"
    )

    def __str__(self):
        return f"{self.content[:50]}{'...' if len(self.content) > 50 else ''}"

    class Meta:
        ordering = ["is_done", "-datetime"]
