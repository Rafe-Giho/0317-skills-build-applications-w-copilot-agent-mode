from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class OctofitCollectionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Marvel Team', universe='marvel', motto='Assemble and train.')
        self.user = UserProfile.objects.create(
            name='Peter Parker',
            email='spiderman@test.dev',
            hero_name='Spider-Man',
            team=self.team,
            points=100,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Web Swing Cardio',
            duration_minutes=45,
            calories_burned=480,
        )
        LeaderboardEntry.objects.create(user=self.user, rank=1, score=100)
        WorkoutSuggestion.objects.create(
            user=self.user,
            title='Wall-Crawl HIIT',
            description='Climb and sprint intervals.',
            intensity='high',
        )

    def test_api_root_lists_all_collection_endpoints(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('users', payload)
        self.assertIn('teams', payload)
        self.assertIn('activities', payload)
        self.assertIn('leaderboard', payload)
        self.assertIn('workouts', payload)

    def test_root_path_points_to_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('users', payload)
        self.assertIn('teams', payload)
        self.assertIn('activities', payload)
        self.assertIn('leaderboard', payload)
        self.assertIn('workouts', payload)

    def test_all_collection_endpoints_return_data(self):
        endpoints = [
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]
        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200)
            self.assertGreaterEqual(len(response.data), 1)
