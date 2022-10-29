from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """The projects homepage. Nothing more."""
    template_name = "home.html"
