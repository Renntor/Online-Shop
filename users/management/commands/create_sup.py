from django.core.management import BaseCommand
from users.models import User
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('USER_EMAIL'),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('USER_PASSWORD'))
        user.save()