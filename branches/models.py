from django.db import models


class Branch(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("ARCHIVED", "Archived"),
    ]

    name = models.CharField(max_length=255)

    city = models.CharField(max_length=255)

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return self.name