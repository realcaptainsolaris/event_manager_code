from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
import factory

from users.factories import UserFactory
from . import models

User = get_user_model()
categories = [
    "Sports",
    "Talk",
    "Cooking",
    "Freetime",
    "Hiking",
    "Movies",
    "Travelling",
    "Science",
    "Arts",
    "Pets",
    "Music",
    "Wellness",
    "Religion",
]


class CategoryFactory(factory.django.DjangoModelFactory):
    """Erstellt eine Kategorie aus einer vorgegebenen Liste."""

    class Meta:
        model = models.Category
        django_get_or_create = ("name",)

    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=20)


class EventFactory(factory.django.DjangoModelFactory):
    """Event Fabrik zum Erstellen eines neuen Events."""

    class Meta:
        model = models.Event

    # Author und Category werden nur erzeugt, wenn sie beim Erstellen der
    # Factory nicht überschrieben werden.
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)

    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=20)
    min_group = factory.Faker("random_element", elements=models.Event.Group)

    date = factory.Faker(
        "date_time_between",
        end_date=timezone.now() + timedelta(days=60),
        start_date=timezone.now() + timedelta(days=1),
        tzinfo=timezone.get_current_timezone(),
    )
