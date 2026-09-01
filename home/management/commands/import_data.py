from django.core.management.base import BaseCommand
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = "Import VETRA data from data.json"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            "data.json"
        )

        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR("data.json not found")
            )
            return

        call_command("loaddata", file_path)

        self.stdout.write(
            self.style.SUCCESS("Data imported successfully!")
        )