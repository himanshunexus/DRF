from django.core.management.base import BaseCommand
from api.models import Singer, Song

class Command(BaseCommand):
    help = "Create original singer/song practice data"

    def handle(self, *args, **options):
        singer, _ = Singer.objects.get_or_create(name="Practice Singer", defaults={"gender": ""})
        Song.objects.get_or_create(title="Morning Practice", singer=singer, defaults={"duration": 180})
        Song.objects.get_or_create(title="Evening Practice", singer=singer, defaults={"duration": 240})
        self.stdout.write("Singer/song examples ready.")


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Run python manage.py seed_music after migrate. Repeating it reuses existing examples.
# The titles are original practice data, not lyrics or the instructor's dataset.
