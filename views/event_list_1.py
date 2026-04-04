class EventListView(ListView):
    """
    Auflisten aller Events

    /events
    """

    model = Event
    template_name = "events/event_liste.html"
