from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class StringIdModelSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(StringIdModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe', 'motto']


class UserProfileSerializer(StringIdModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(
        source='team',
        queryset=Team.objects.all(),
        required=False,
        allow_null=True,
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['team_id'] = str(instance.team_id) if instance.team_id else None
        return data

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'hero_name', 'team_id', 'points']


class ActivitySerializer(StringIdModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=UserProfile.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user_id'] = str(instance.user_id)
        return data

    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration_minutes', 'calories_burned', 'logged_at']


class LeaderboardEntrySerializer(StringIdModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=UserProfile.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user_id'] = str(instance.user_id)
        return data

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user_id', 'rank', 'score']


class WorkoutSuggestionSerializer(StringIdModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=UserProfile.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user_id'] = str(instance.user_id)
        return data

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user_id', 'title', 'description', 'intensity']
