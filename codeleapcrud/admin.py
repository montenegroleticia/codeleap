from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "created_datetime")
    search_fields = ("username", "title")
    list_filter = ("created_datetime",)
