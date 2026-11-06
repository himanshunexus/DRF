from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .forms import UserForm
from .models import User
from .serializers import UserSerializer

@staff_member_required
def home(request, pk=None):
    record = get_object_or_404(User, pk=pk) if pk else None
    form = UserForm(request.POST or None, instance=record)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("enroll-home")
    return render(request, "enroll/home.html", {"form": form, "records": User.objects.order_by("id")})

@staff_member_required
@require_POST
def delete(request, pk):
    get_object_or_404(User, pk=pk).delete()
    return redirect("enroll-home")

class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# home handles the existing HTML create/update interface; delete requires POST plus CSRF.
# UserViewSet exposes the same records at /api/crud/ using the same database model.
# The staff policy is an original companion addition because these rows contain personal data.
# Create a superuser, log in at /admin/, then open /enroll/ to try the form.
# The instructor's existing app uses class-based ModelForm views; this short companion uses
# functions for the HTML layer, while preserving the API-to-existing-model teaching point.
# Session writes need CSRF. Basic authentication is for local testing; HTTPS is required remotely.
