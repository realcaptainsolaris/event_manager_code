from django.contrib import admin
from .models import Category, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_filter = ("category",)
    list_display = "slug", "author", "name", "category", "is_active"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_display = "id", "name", "sub_title", "slug"
    list_display_links = ("name", "sub_title")
    list_filter = ("events", "sub_title")
    search_fields = ["name"]
