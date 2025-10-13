from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from personnel.models import Employe

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Employe.objects.get_or_create(user=user, defaults={
                'nom': user.username,
                'prenom': '',
                'email': user.email
            })
        return user
