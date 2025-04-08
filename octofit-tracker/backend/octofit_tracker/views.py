from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

# Establish a connection to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/'
    })

@api_view(['GET'])
def get_users(request):
    users = db['users'].find()
    serialized_users = [UserSerializer(user).to_representation() for user in users]
    return Response(serialized_users)

@api_view(['GET'])
def get_teams(request):
    teams = db['teams'].find()
    serialized_teams = [TeamSerializer(team).to_representation() for team in teams]
    return Response(serialized_teams)

@api_view(['GET'])
def get_activities(request):
    activities = db['activities'].find()
    serialized_activities = [ActivitySerializer(activity).to_representation() for activity in activities]
    return Response(serialized_activities)

@api_view(['GET'])
def get_leaderboard(request):
    leaderboard = db['leaderboard'].find()
    serialized_leaderboard = [LeaderboardSerializer(entry).to_representation() for entry in leaderboard]
    return Response(serialized_leaderboard)

@api_view(['GET'])
def get_workouts(request):
    workouts = db['workouts'].find()
    serialized_workouts = [WorkoutSerializer(workout).to_representation() for workout in workouts]
    return Response(serialized_workouts)
