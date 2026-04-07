"""
Erzeugen von Event-Daten

Dieses Modul stellt ein Management-Kommando bereit, um zufällige Event-Daten zu generieren.
Dabei werden ``factory_boy`` und die Bibliothek ``Faker`` verwendet.
"""

import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from events.factories import CategoryFactory, EventFactory
from events.models import Category, Event


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.description = "Generate Random Events and Categories"
        parser.add_argument(
            "-e",
            "--events",
            type=int,
            help="Number of events to be generated",
            required=True,
        )
        parser.add_argument(
            "-c",
            "--categories",
            type=int,
            help="Number of categories to be generated, max is 10",
            required=True,
        )
        parser.epilog = "Usage example: python manage.py create_events -e 10 -c 3"

    def handle(self, *args, **options):
        num_events: int = options["events"]
        num_categories: int = options["categories"]

        if num_events < 0 or not 0 <= num_categories <= 10:
            raise SystemExit(
                "Nur nicht-negative Werte und maximal 10 Kategorien erlaubt."
            )

        print(f"Generating events={num_events}, categories={num_categories}")

        User = get_user_model()
        users = list(User.objects.all())

        if not users:
            raise SystemExit(
                "Keine User vorhanden. Bitte zuerst: manage.py set_testusers"
            )

        print("Lösche vorhandene Daten...")
        Event.objects.all().delete()
        Category.objects.all().delete()

        print("Erstelle Kategorien...")
        categories = CategoryFactory.create_batch(num_categories)

        print("Erstelle Events...")
        for _ in range(num_events):
            event = EventFactory(
                category=random.choice(categories),
                author=random.choice(users),
            )
            print(f"=> {event}")
