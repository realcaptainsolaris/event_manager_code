from django.contrib import admin
from .models import Category, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ("category",)
    list_display = "author", "name", "category", "is_active"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "sub_title"
    list_display_links = ("name", "sub_title")
    list_filter = ("events", "sub_title")
    search_fields = ["name"]
