from django import forms
from ..models import User
def uniqueEmail(email):
    if len(User.objects.filter(email = email)) > 0:
        raise forms.ValidationError("Email should be unique")
    return email
