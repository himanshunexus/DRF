from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This lesson is only about output, so create/update methods are deliberately absent.
# StudentSerializer is an ordinary Serializer, with each field written explicitly.
# name/city become text and roll becomes an integer in serializer.data.
# We keep a read-only id as a companion addition so you can follow detail URLs.
# Pass a model instance for one result, or a queryset and many=True for several.
# The serializer produces Python values; JSONRenderer/JsonResponse encode them.
# The reviewed lecture uses the same Student/name/roll/city vocabulary.
# Deserialization and saving are introduced in the next relevant lessons.
