import requests

BASE_URL = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    path = "students/" if id is None else f"students/{id}/"
    response = requests.get(BASE_URL + path, timeout=10)
    response.raise_for_status()
    return response.json()


def write_data(method, path, data=None):
    with requests.Session() as client:
        cookie_response = client.get(BASE_URL + "csrf/", timeout=10)
        cookie_response.raise_for_status()
        headers = {"X-CSRFToken": client.cookies["csrftoken"]}
        response = client.request(method, BASE_URL + path, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return None if response.status_code == 204 else response.json()


def post_data(data):
    return write_data("POST", "student-create/", data)


def update_data(id, data):
    return write_data("PATCH", f"students/{id}/", data)


def delete_data(id):
    return write_data("DELETE", f"students/{id}/")


if __name__ == "__main__":
    print(get_data())


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Start the server separately. Running this file only reads records; writes are explicit.
# In a Python shell import post_data and pass a name/roll/city dictionary to insert.
# get_data uses URL ids, not a GET body, to work with normal HTTP clients and caches.
# requests.Session keeps the CSRF cookie; the header proves the client read that cookie.
# json=data encodes the dictionary and sets the JSON Content-Type automatically.
# PATCH changes only supplied fields. A 204 deletion has no JSON body to parse.
# The helper names follow the reviewed workflow; the implementation and CSRF handling are original.
