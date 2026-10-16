from django.conf import settings
from django.db import models
from django.utils import timezone


class Voetbalspelers(models.Model):
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    naam = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    aangemaakt_datum = models.DateTimeField(default=timezone.now)
    gewijzigd_datum = models.DateTimeField(blank=True, null=True)

    def publiceren(self):
        self.gewijzigd_datum = timezone.now()
        self.save()

    def __str__(self):
        return self.naam