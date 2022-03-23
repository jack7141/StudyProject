import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from accounts import models as user_models
from arts import models as art_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        arts = art_models.Art.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "review": lambda x: seeder.faker.sentence(),
                "art": lambda x: random.choice(arts),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))