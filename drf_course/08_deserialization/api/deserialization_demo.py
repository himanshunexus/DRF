from io import BytesIO
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer


def insert_student():
    body = b'{"name":"Mira","roll":801,"city":"Pune"}'
    data = JSONParser().parse(BytesIO(body))
    serializer = StudentSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


# NOTES ABOUT THE COMPLETE CODE ABOVE
# BytesIO treats bytes as a file-like input stream. JSONParser reads it into a dictionary.
# data= means we are supplying input, not serializing an existing object.
# is_valid populates validated_data and reports field errors; save calls create.
# Call from manage.py shell: from api.deserialization_demo import insert_student; insert_student().
# Run once: running again with roll 801 correctly fails the unique-roll validation.
# In normal DRF views request.data already performs parsing; do not repeat this manually.
