from django.db import models


class Incident(models.Model):

    SEVERITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In Progress"),
        ("CLOSED", "Closed"),
    ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="LOW"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title