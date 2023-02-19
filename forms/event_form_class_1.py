from django import forms
from django.core.exceptions import ValidationError
from .models import Event, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
