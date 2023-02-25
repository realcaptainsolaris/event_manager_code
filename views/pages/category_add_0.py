from django.shortcuts import get_object_or_404, render, reverse
from .forms import CategoryForm


def category_create(request):
    """Eine View zum Hinzufügen einer Kategorie."""
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return (
                redirect("events:category_detail", kwargs={"id": self.category.id}),
            )
    else:
        form = CategoryForm()
    return render(
        request,
        "events/category_add.html",
        {"form": form},
    )
