from django.core.management.base import BaseCommand
from api.field_playground import FieldPlaygroundSerializer


class Command(BaseCommand):
    help = "Demonstrate serializer fields without writing to the database."

    def handle(self, *args, **options):
        serializer = FieldPlaygroundSerializer(data={
            "name": "  Riya  ", "email": "riya@example.com", "note": None,
            "reference": "12345678-1234-5678-1234-567812345678",
        })
        serializer.is_valid(raise_exception=True)
        self.stdout.write(repr(serializer.validated_data))
        self.stdout.write(repr(serializer.data))


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Run python manage.py field_demo. It prints two different stages of serialization.
# validated_data contains converted Python types, including a UUID object.
# data contains output-friendly values, including the UUID string and display_name.
# The example intentionally contains no password so the command does not print secrets.
