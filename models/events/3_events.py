from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from event_manager.utils import slugify_instance_name


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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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


@receiver(pre_save, sender=Event)
def create_slug(sender, instance, *args, **kwargs):
    print("pre save wurde ausgeführt")
    if not instance.slug:
        instance.slug = slugify_instance_name(instance, new_slug=None)
