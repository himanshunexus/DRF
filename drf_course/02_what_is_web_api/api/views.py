from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def student_list(request):
    return Response({"id": 1, "name": "Asha", "roll": 101, "city": "Delhi"})


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The decorator allows only GET. DRF returns HTTP 405 for other methods.
# The function receives a request and returns a Python dictionary in a Response.
# DRF renders that dictionary as JSON when the client requests application/json.
# This first demo is deliberately static: there is no database lookup in this view.
# A browser, mobile app or Python client can call the same URL.
# Modern version note: this example runs on Django 5.2 LTS and DRF 3.16.
