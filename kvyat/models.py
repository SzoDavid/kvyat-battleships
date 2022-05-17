from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    guesses = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def points(self):
        return (((49 * self.games_played) - self.guesses) * 10) / \
               (self.games_played + ((timezone.now() - self.user.date_joined).days / 14) + 1)

    def points_round(self):
        return round(self.points())

    def average_guesses(self):
        return round((self.guesses / self.games_played), 2)

    def weeks_since_joined(self):
        return (timezone.now() - self.user.date_joined).days // 7


