from django.contrib import admin
from .models import Category, Event, Review


class ReviewInlineAdmin(admin.TabularInline):
    model = Review


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ReviewInlineAdmin]
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "date",
        "slug",
        "author",
        "name",
        "category",
        "category_slug",
        "is_active",
    )
    list_filter = ("category",)
    search_fields = ["name"]
    actions = ["make_active", "make_inactive"]
    readonly_fields = ("author",)
    list_display_links = ("name", "slug")
    radio_fields = {
        "category": admin.HORIZONTAL,
        "min_group": admin.VERTICAL,
    }
    autocomplete_fields = ['category']

    @admin.action(description="Setze Events active")
    def make_active(self, request, queryset):
        """Set all Entries to active."""
        queryset.update(is_active=True)

    @admin.action(description="Setze Events inactive")
    def make_inactive(self, request, queryset):
        """Set all Entries to inactive."""
        queryset.update(is_active=False)

    @admin.display(description="Kategorie Slug")
    def category_slug(self, obj):
        return obj.category.slug


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_display = "id", "name", "sub_title", "slug"
    list_display_links = ("name", "sub_title")
    list_filter = ("events", "sub_title")
    search_fields = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = "author", "rating", "event_name"
    search_fields = ["event__name", "review"]

    @admin.display(description="Event Name")
    def event_name(self, obj):
        return obj.event.name
