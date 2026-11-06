import requests

URL = "http://127.0.0.1:8000/stuinfo/1/"


def get_data():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(get_data())


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Start this lesson's server in a different terminal, then run python myapp.py.
# This is a client, not a Django view: it makes a real HTTP request to the server.
# URL selects one student; use /stuinfo/ instead to request all students.
# requests.get sends GET. timeout prevents an indefinite wait on a broken server.
# raise_for_status surfaces HTTP errors before we try to use the response body.
# response.json() parses returned JSON into a Python dictionary or list.
# The main guard prevents an HTTP request merely from importing this file.
# myapp.py and requests.get were visible in the reviewed lesson; this client is original.
