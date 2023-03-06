def category_update(request, pk):
    """View zum Ändern einer Kategorie."""
    instance = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=instance)

    if form.is_valid():
        category = form.save()
        return (redirect("events:category_detail", kwargs={"id": self.category.id}),)

    return render(
        request,
        "events/category_add.html",
        {"form": form},
    )
