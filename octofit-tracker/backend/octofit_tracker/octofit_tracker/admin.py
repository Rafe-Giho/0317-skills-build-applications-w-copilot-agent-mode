from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'universe')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'hero_name', 'email', 'team', 'points')
	search_fields = ('hero_name', 'email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
	list_display = ('id', 'rank', 'user', 'score')
	ordering = ('rank',)


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'title', 'intensity')
