from django.contrib import admin
from .models import Player
# Register your models here.

@admin.register(Player)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('email',"name","role")