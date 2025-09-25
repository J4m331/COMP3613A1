from App.models import Leaderboard
from App.database import db

def display_leaderboard():
    students = []
    for s in Leaderboard.students:
        students.append(s)
    for s in students:
        s.get_json()
    return