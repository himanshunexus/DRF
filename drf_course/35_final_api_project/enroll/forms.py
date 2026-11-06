from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["name", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].required = not bool(self.instance.pk)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.password = make_password(password)
        elif user.pk:
            user.password = User.objects.get(pk=user.pk).password
        if commit:
            user.save()
        return user


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The ModelForm validates name/email and requires an initial password of at least 8 characters.
# PasswordInput never renders the stored value. On edit, blank means preserve the old hash.
# make_password hashes a newly entered value before saving it; the form never stores plaintext.
# The API serializer independently applies the same storage rule.
