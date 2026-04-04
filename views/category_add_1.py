from django.shortcuts import render, redirect
from .forms import CategoryForm


def category_create(request):
    """
    Eine View zum Hinzufügen einer Kategorie.

    events/category/create
    """
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
