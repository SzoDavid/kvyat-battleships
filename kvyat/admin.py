from django.contrib import admin

from .models import UserData


class UserDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['user']}),
        ('Stats', {'fields': ['games_played', 'guesses']}),
    ]
    search_fields = ['get_username']
    list_display = ('get_username', 'games_played', 'guesses', 'points_round')

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.user.username


admin.site.register(UserData, UserDataAdmin)
