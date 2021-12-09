from django.core.management.base import BaseCommand, CommandError
from anciens.models import Ancien

import csv

class Command(BaseCommand):
    help = "Run that to load a csv"

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **options):
        with open(options["csv_path"]) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Ancien.objects.get_or_create(
                    nom=row[0],
                    prenom=row[1],
                    promo=row[2],
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created