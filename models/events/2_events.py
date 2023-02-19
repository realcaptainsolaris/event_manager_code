from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


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

    def __str__(self):
        return self.name


class Event(DateMixin):
    """Der Event, der auf einen bestimmten Zeitpunkt terminiert ist."""

    class Group(models.IntegerChoices):
        SMALL = 2
        MEDIUM = 5
        BIG = 10
        LARGE = 20
        UNLIMITED = 0

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

    def __str__(self):
        return self.name
