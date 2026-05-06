from django.shortcuts import redirect, render

from .forms import CategoryForm
from .models import Category, Event


def category_create(request):
    """
    Eine View zum Hinzufügen einer Kategorie.

    events/category/create
    """
    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        category = form.save()
        return redirect(category)

    return render(request, "events/category_create.html", {"form": form})
