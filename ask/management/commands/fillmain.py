from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ask.fill import Fill

class Command(BaseCommand):
    def handle(self, *args, **options):
        fill = Fill()
        for i in range(50):
            user = fill.create_profile()
            fill.ask(user)
            fill.answer(user)
