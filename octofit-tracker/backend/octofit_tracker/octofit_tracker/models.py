from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)
    motto = models.CharField(max_length=200)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.hero_name} ({self.email})"


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    logged_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.user.hero_name}"


class LeaderboardEntry(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entry')
    rank = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"#{self.rank} {self.user.hero_name}"


class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=120)
    description = models.TextField()
    intensity = models.CharField(max_length=30)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.title} ({self.user.hero_name})"
