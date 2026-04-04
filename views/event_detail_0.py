from django.views.generic.detail import DetailView


class EventDetailView(DetailView):
    """
    events/event/3
    """

    model = Event
