from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView

from .forms import EventForm
from .models import Category, Event


class EventCreateView(LoginRequiredMixin, CreateView):
    """
    Erstellt ein Event für eine bestimmte Kategorie

    events/event/create/<category_id>
    """

    model = Event
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        """Setze die Kategorie für den Event, bevor die Anfrage verarbeitet wird."""
        self.category = get_object_or_404(Category, pk=self.kwargs["category_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Setze die Kategorie und den Autor für den Event, bevor das Formular gespeichert wird."""
        form.instance.category = self.category
        form.instance.author = self.request.user
        return super().form_valid(form)
