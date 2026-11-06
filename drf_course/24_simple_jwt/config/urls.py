from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns += [
    path("gettoken/", TokenObtainPairView.as_view()),
    path("refreshtoken/", TokenRefreshView.as_view()),
    path("verifytoken/", TokenVerifyView.as_view()),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The project URLconf delegates /api/ to the lesson app.
# /admin/ is Django's staff administration interface.
# /api-auth/login/ and logout routes support session login for the browsable API.
# include removes the matched prefix before passing the remaining URL to the app.
# Use trailing slashes in examples; redirects are especially awkward for POST bodies.
# Modern version note: django.urls.path replaces older regex-only url() examples.
#
# gettoken/refreshtoken/verifytoken are lecture-named aliases for Simple JWT obtain/refresh/verify views.
