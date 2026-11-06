from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from api.models import Student


class Command(BaseCommand):
    help = "Create local-only demo users and five students without overwriting existing rows."

    def handle(self, *args, **options):
        User = get_user_model()
        for username, password, staff in [
            ("learner", "learn-local-123", False),
            ("teacher", "teach-local-123", True),
        ]:
            user, created = User.objects.get_or_create(username=username, defaults={"is_staff": staff})
            if created:
                user.set_password(password)
                user.save()
        owner = User.objects.get(username="learner")
        for roll, name, city in [
            (101, "Asha", "Delhi"), (102, "Ravi", "Pune"), (103, "Mira", "Delhi"),
            (104, "Kabir", "Jaipur"), (105, "Neha", "Mumbai"),
        ]:
            defaults = {"name": name, "city": city}
            defaults["owner"] = owner
            Student.objects.get_or_create(roll=roll, defaults=defaults)
        self.stdout.write(self.style.SUCCESS("Demo data ready. See README.md for local credentials."))


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Run python manage.py seed after migrate. Django discovers this file as the seed command.
# get_or_create keeps repeated runs from duplicating our sample rows or changing existing passwords.
# set_password hashes the demo password; never assign raw text directly to user.password.
# learner is a normal user; teacher is staff but not a superuser.
# These published credentials are for local practice only. Never seed a public deployment with them.
# Five rows make pagination, search and filtering visible immediately.
