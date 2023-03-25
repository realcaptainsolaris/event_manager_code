from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_id = "event_form"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-8"
        self.helper.add_input(Submit("submit", "Submit"))

        self.helper.layout = Layout(
            Fieldset(
                "Standard Infos",
                "name",
                "date",
                "category",
                css_class="form-group",
            ),
            Fieldset(
                "Detail Infos",
                "description",
                "min_group",
                "sub_title",
                "is_active",
                HTML(
                    """
                    <div class='mb-3 row'>
                    <div class='col-lg-2'></div>
                    <div class='col-lg-8'>Danke für die Mitarbeit, <strong>Wir
                    finden das ganz toll!</strong></div>
                    </div>
                    """
                ),
                css_class="form-group",
            ),
        )

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

    def clean_sub_title(self) -> str:
        sub_title = self.cleaned_data["sub_title"]
        illegal = ("*", "-", ":")
        if isinstance(sub_title, str) and sub_title.startswith(illegal):
            raise ValidationError("Dieses Zeichen ist nicht erlaubt!")

        return sub_title
