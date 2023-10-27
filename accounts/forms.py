
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customuser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customuser
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customuser
        fields = (
            "email",
            "username",
        )
