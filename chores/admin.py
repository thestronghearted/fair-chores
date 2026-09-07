from django.contrib import admin

from .models import Chore, Claim, Vote


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ("title", "is_recurring", "scheduled_for", "created_by")
    list_filter = ("is_recurring",)
    search_fields = ("title", "description")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("chore", "member", "points", "created_at")
    list_filter = ("chore",)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ("chore", "member", "mode", "week_start", "is_active")
    list_filter = ("mode", "is_active")
