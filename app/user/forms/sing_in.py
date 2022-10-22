from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


class SingInForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password."
        ),
        "inactive": _("This account is inactive."),
    }
