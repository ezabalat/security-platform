from django.shortcuts import render

from .models import Incident


def dashboard(request):

    incidents = Incident.objects.all()

    total_incidents = incidents.count()

    return render(
        request,
        "dashboard.html",
        {
            "incidents": incidents,
            "total_incidents": total_incidents
        }
    )