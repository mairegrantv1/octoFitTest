from bson import ObjectId

class ObjectIdField:
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return {
            "_id": str(self.data["_id"]),
            "name": self.data["name"],
            "email": self.data["email"]
        }

class TeamSerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return {
            "_id": str(self.data["_id"]),
            "name": self.data["name"],
            "members": [UserSerializer(member).to_representation() for member in self.data["members"]]
        }

class ActivitySerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return {
            "_id": str(self.data["_id"]),
            "user": str(self.data["user"]),
            "type": self.data["type"],
            "duration": self.data["duration"]
        }

class LeaderboardSerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return {
            "_id": str(self.data["_id"]),
            "user": str(self.data["user"]),
            "score": self.data["score"]
        }

class WorkoutSerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return {
            "_id": str(self.data["_id"]),
            "name": self.data["name"],
            "calories_burned": self.data["calories_burned"]
        }
