"""
Generating Event Data.

This module provides a management command to generate random
event data built with factory boy and the faker libary.
"""

import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from events.factories import CategoryFactory
from events.factories import EventFactory
from events.factories import ReviewFactory
from events.models import Category
from events.models import Event
from events.models import Review


CATEGORIES = 4
EVENTS = 20
MAX_REVIEWS = 7
MIN_RATING = 1
MAX_RATING = 6


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.description = "Generate Random Events and Categories"
        parser.add_argument(
            '-e',
            '--events',
            type=int,
            help='Number of events to be generated',
        )
        parser.add_argument(
            '-c',
            '--categories',
            type=int,
            help='Number of categories to be generated, max is 10',
        )
        parser.epilog = (
            "Usage example: python manage.py create_events events=100 "
            "categories=10"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        num_events = n if (n := options.get("events")) else EVENTS
        num_categories = n if (
            n := options.get("categories")) else CATEGORIES

        if any([num_events < 0,
                num_categories < 0,
                num_categories > 10
                ]):
            raise ValueError(("Negative Werte nicht erlaubt. Nur maximal 10"
                             " Kategorien"))

        print(
            f"Generating {num_events=} {num_categories=} "
        )
        user_list = get_user_model().objects.all()

        if not user_list:
            print("Es existieren keine User im System.")
            print("Bitte führe erst python manage.py set_testusers aus")
            raise SystemExit(1)

        print("Lösche Model Data...")
        for m in [Review, Event, Category]:
            m.objects.all().delete()

        print("Erstelle Kategorien...")
        categories = CategoryFactory.create_batch(num_categories)

        print("Erstelle Events...")
        for _ in range(num_events):
            event = EventFactory(
                category=random.choice(categories),
                author=random.choice(user_list),
            )

            # each event can have up to MAX_REVIEWS reviews
            for _ in range(random.randint(0, MAX_REVIEWS)):
                ReviewFactory(event=event,
                              author=random.choice(user_list),
                              rating=random.randint(MIN_RATING,
                                                    MAX_RATING),
                              ),
