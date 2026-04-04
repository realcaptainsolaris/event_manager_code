def category_update(request, pk):
    """
    View zum Ändern einer Kategorie.

    events/category/7/update
    """
    instance = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=instance)

    if form.is_valid():
        category = form.save()
        return redirect("events:category_detail", pk=category.pk)

    return render(
        request,
        "events/category_update.html",
        {"form": form},
    )
