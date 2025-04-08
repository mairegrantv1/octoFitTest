from django.urls import path
from .views import api_root, get_users, get_teams, get_activities, get_leaderboard, get_workouts

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/users/', get_users, name='get-users'),
    path('api/teams/', get_teams, name='get-teams'),
    path('api/activities/', get_activities, name='get-activities'),
    path('api/leaderboard/', get_leaderboard, name='get-leaderboard'),
    path('api/workouts/', get_workouts, name='get-workouts'),
]
