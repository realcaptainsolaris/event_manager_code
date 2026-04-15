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
        exclude = ("category", "author")

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
        }

        labels = {
            "name": "Name des Events",
            "sub_title": "Slogan",
            "description": "Kurzbeschreibung",
            "date": "Datum des Events",
        }

    def clean_sub_title(self):
        sub_title = self.cleaned_data["sub_title"]
        illegal = ("*", "-", ":")
        if isinstance(sub_title, str) and sub_title.startswith(illegal):
            raise ValidationError("Dieses Zeichen ist nicht erlaubt!")

        return sub_title
