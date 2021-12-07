from django.contrib import admin

from .models import UserData, Room, Field


class FieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['user']}),
        ('Fields', {'fields': ['play_field', 'selected_field']}),
    ]
    search_fields = ['get_username']
    list_display = ['get_username']

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.user.username


class UserDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['user']}),
        ('Stats', {'fields': ['games_played', 'games_won']}),
    ]
    search_fields = ['get_username']
    list_display = ('get_username', 'games_played', 'games_won', 'points')

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.user.username


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['password']}),
        ('Players', {'fields': ['host', 'guest']}),
    ]
    list_display = ('pk', 'get_host_username', 'get_guest_username')

    @admin.display(description='Host')
    def get_host_username(self, obj):
        return obj.host.user.username

    @admin.display(description='Guest')
    def get_guest_username(self, obj):
        return obj.guest.user.username


admin.site.register(UserData, UserDataAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Field, FieldAdmin)
