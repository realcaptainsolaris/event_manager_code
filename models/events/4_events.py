from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
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
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    slug = models.SlugField(unique=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    min_group = models.IntegerField(choices=Group.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def related_events(self):
        """
        Ähnliche Events aus der gleichen Kategorie und der selben 
        min-group. 
        """
        number = 5
        related_events = Event.objects.filter(
            min_group__exact=self.min_group, category=self.category
        )
        return related_events.exclude(pk=self.id)[:number]

    @property
    def has_finished(self) -> bool:
        """Wenn das Event in der Vergangenheit liegt, return True."""
        now = timezone.now()
        return self.date <= now
