from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        WorkoutSuggestion.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(name='Marvel Team', universe='marvel', motto='Avengers, assemble your fitness!')
        dc = Team.objects.create(name='DC Team', universe='dc', motto='Train like the Justice League!')

        heroes = [
            {
                'name': 'Peter Parker',
                'email': 'spiderman@octofit.dev',
                'hero_name': 'Spider-Man',
                'team': marvel,
                'points': 210,
                'activity': ('Web Swing Cardio', 45, 480),
                'workout': ('Wall-Crawl HIIT', '4 rounds of climb, sprint, and jump drills.', 'high'),
            },
            {
                'name': 'Natasha Romanoff',
                'email': 'blackwidow@octofit.dev',
                'hero_name': 'Black Widow',
                'team': marvel,
                'points': 190,
                'activity': ('Combat Circuit', 40, 420),
                'workout': ('Widow Agility Flow', 'Core stability with agility ladder intervals.', 'medium'),
            },
            {
                'name': 'Bruce Wayne',
                'email': 'batman@octofit.dev',
                'hero_name': 'Batman',
                'team': dc,
                'points': 230,
                'activity': ('Night Patrol Run', 50, 530),
                'workout': ('Gotham Strength Session', 'Compound lifts and tactical conditioning.', 'high'),
            },
            {
                'name': 'Diana Prince',
                'email': 'wonderwoman@octofit.dev',
                'hero_name': 'Wonder Woman',
                'team': dc,
                'points': 240,
                'activity': ('Amazon Endurance', 55, 560),
                'workout': ('Lasso Mobility Set', 'Mobility + full-body endurance superset.', 'medium'),
            },
        ]

        created_users = []
        for hero in heroes:
            user = UserProfile.objects.create(
                name=hero['name'],
                email=hero['email'],
                hero_name=hero['hero_name'],
                team=hero['team'],
                points=hero['points'],
            )
            created_users.append(user)

            activity_name, duration, calories = hero['activity']
            Activity.objects.create(
                user=user,
                activity_type=activity_name,
                duration_minutes=duration,
                calories_burned=calories,
            )

            workout_title, workout_description, workout_intensity = hero['workout']
            WorkoutSuggestion.objects.create(
                user=user,
                title=workout_title,
                description=workout_description,
                intensity=workout_intensity,
            )

        ranking = sorted(created_users, key=lambda item: item.points, reverse=True)
        for index, user in enumerate(ranking, start=1):
            LeaderboardEntry.objects.create(user=user, rank=index, score=user.points)

        self.stdout.write(self.style.SUCCESS('테스트 데이터 적재 완료'))
