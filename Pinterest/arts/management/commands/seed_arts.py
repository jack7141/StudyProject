import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from arts import models as arts_models
from accounts import models as user_models
from django.contrib.admin.utils import flatten

class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            arts_models.Art,
            number,
            {
                "title": lambda x: seeder.faker.name(),
                "description": lambda x: seeder.faker.sentence(),
                "artist": lambda x: random.choice(all_users),
                "file":f"art_work/{random.randint(1, 31)}.jpg",
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        # for pk in created_clean:
        #     room = arts_models.Art.objects.get(pk=pk)
        #     for i in range(3, random.randint(10, 30)):
        #         arts_models.Art.objects.create(
        #             title=room,
        #             file=f"art_work/{random.randint(1, 31)}.jpg",
        #         )

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))