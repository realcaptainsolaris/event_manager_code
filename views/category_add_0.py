from django.shortcuts import get_object_or_404, render, reverse, redirect
from .forms import CategoryForm
from .models import Event, Category
from .forms import CategoryForm


def category_create(request):
    """Eine View zum Hinzufügen einer Kategorie.

    http://127.0.0.1:8000/events/category/create

    """
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            category = form.save()
            return redirect("events:category_detail", pk=category.pk)
    else:
        form = CategoryForm()
    return render(
        request,
        "events/category_create.html",
        {"form": form},
    )
