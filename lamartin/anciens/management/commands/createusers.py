from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from anciens.models import Ancien

import csv

class Command(BaseCommand):
    help = "Run that to load a csv"

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **options):
        created=0
        linked=0
        with open(options["csv_path"]) as f:
            reader = csv.reader(f)
            for row in reader:
                nom=row[0]
                prenom=row[1]
                birth=row[3]
                promo=row[2]
                username = f"{prenom.lower()}.{nom.lower()}"
                if not User.objects.filter(username=username).exists():
                    new_user =  User.objects.create_user(username, password=f"{birth}.{promo}")
                    created+=1
                    if Ancien.objects.filter(nom__iexact=nom, prenom__iexact=prenom, promo=promo).exists():
                        ancien =  Ancien.objects.get(nom__iexact=nom, prenom__iexact=prenom, promo=promo)
                        ancien.user = new_user
                        ancien.save()
                        linked+=1
                else:
                    user =  User.objects.get(username=username)
                    user.set_password(f"{birth}.{promo}")
                    user.save(  )
            print(f"{created} users created, {linked} anciens linked")