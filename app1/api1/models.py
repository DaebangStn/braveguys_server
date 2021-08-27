from django.db import models


class State(models.Model):
    motor = models.BooleanField(default=False)