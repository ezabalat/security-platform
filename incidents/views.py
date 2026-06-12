from django.shortcuts import render

from .models import Incident


def dashboard(request):

    incidents = Incident.objects.all()

    return render(
        request,
        "dashboard.html",
        {
            "incidents": incidents
        }
    )