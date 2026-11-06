from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The project URLconf delegates /api/ to the lesson app.
# /admin/ is Django's staff administration interface.
# /api-auth/login/ and logout routes support session login for the browsable API.
# include removes the matched prefix before passing the remaining URL to the app.
# Use trailing slashes in examples; redirects are especially awkward for POST bodies.
# Modern version note: django.urls.path replaces older regex-only url() examples.
