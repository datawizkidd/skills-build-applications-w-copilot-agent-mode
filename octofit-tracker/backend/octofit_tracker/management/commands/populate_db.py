from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thunder God", "password": "thundergodpassword"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Metal Geek", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Zero Cool", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "email": "crashoverride@hmhigh.edu", "name": "Crash Override", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "Sleep Token", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Team Beta", "members": [users[2]["_id"], users[3]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": 30},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard
        leaderboard = [
            {"_id": ObjectId(), "team": teams[0]["_id"], "score": 100},
            {"_id": ObjectId(), "team": teams[1]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
            {"_id": ObjectId(), "name": "HIIT", "description": "High-intensity interval training for fat loss."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
