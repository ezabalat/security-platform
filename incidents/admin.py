from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "severity",
        "status",
        "created_at"
    )

    list_filter = (
        "severity",
        "status"
    )

    search_fields = (
        "title",
        "description"
    )