class EventListView(ListView):
    """
    Auflisten aller aktiven Events

    /events
    """

    model = Event
    paginate_by = 10

    def get_queryset(self):
        return Event.active.prefetch_related("category").all()
