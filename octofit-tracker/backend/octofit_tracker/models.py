from pymongo import MongoClient

# Establish a connection to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Define collections
users_collection = db['users']
teams_collection = db['teams']
activities_collection = db['activities']
leaderboard_collection = db['leaderboard']
workouts_collection = db['workouts']
