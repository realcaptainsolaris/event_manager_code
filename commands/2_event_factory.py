import random
import arrow
import factory
from django.contrib.auth import get_user_model
from django.utils import timezone
from user.factories import UserFactory
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
    "Pets"
]


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph")


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event

    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    min_group = factory.LazyAttribute(
        lambda _: random.choice(list(models.Event.Group))
    )

    date = factory.Faker(
        "date_time_between",
        end_date=arrow.utcnow().shift(days=+60).datetime,
        start_date=arrow.utcnow().datetime,
        tzinfo=timezone.get_current_timezone(),
    )

class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Review

    review = factory.Faker("paragraph")
