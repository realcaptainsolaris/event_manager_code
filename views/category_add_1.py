from django.shortcuts import get_object_or_404, render, reverse, redirect
from .forms import CategoryForm
from .models import Event, Category
from .forms import CategoryForm


def category_create(request):
    """Eine View zum Hinzufügen einer Kategorie."""
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect(category)
    else:
        form = CategoryForm()
    return render(
        request,
        "events/category_create.html",
        {"form": form},
    )
