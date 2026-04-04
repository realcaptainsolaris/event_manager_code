class EventListView(ListView):
    """
    Auflisten aller Events

    /events
    """

    model = Event
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.prefetch_related("category").all()
