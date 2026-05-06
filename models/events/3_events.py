from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateMixin):
    """Eine Kategorie für einen Event."""

    name = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self) -> str:
        return self.name


class Event(DateMixin):
    """Der Event, der auf einen bestimmten Zeitpunkt terminiert ist."""

    class Group(models.IntegerChoices):
        SMALL = 2, "kleine Gruppe"
        MEDIUM = 5, "mittelgroße Gruppe"
        BIG = 10, "große Gruppe"
        LARGE = 20, "sehr große Gruppe"
        UNLIMITED = 0, "ohne Begrenzung"

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    min_group = models.IntegerField(choices=Group.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
