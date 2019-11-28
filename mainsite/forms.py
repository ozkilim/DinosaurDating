from django import forms
from django.http import request

from mainsite import models
from .models import Atendee


class AtendeeForm(forms.ModelForm):
    class Meta:
        model = Atendee
        fields = ['user_name', 'email','looking_for','age','gender','phone_number' ]

