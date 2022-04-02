from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def points(self):
        return (self.games_won * 10) / (self.games_played + ((timezone.now() - self.user.date_joined).days / 14) + 1)

    def weeks_since_joined(self):
        return (timezone.now() - self.user.date_joined).days // 7


class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    play_field = models.CharField(max_length=200, default='')
    selected_field = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username


class Room(models.Model):
    host = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='host_field')
    guest = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='guest_field')
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)

    @admin.display(
        boolean=True
    )
    def open(self):
        return self.guest is None
