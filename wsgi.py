import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
#from App.models import User
from App.models import *
from App.main import create_app
#from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>

'''
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli
'''
student_cli = AppGroup('student', help='Student user commands')

@student_cli.command("create", help="Creates a new student")
def create_student_command():
    print("Enter a new username")
    username = input()
    print("Enter a password")
    password = input()
    print("Enter a new firstname")
    firstname = input()
    print("Enter a new lastname")
    lastname = input()
    create_student(username, password, firstname, lastname)
    print("New student " + username + " has been created")

@student_cli.command('make_request', help='Create request for logging hours')
def create_request_for_hours():
    print('Please enter Student ID')
    student_id = input()
    print('Please enter hours to be logged')
    hours = input()
    create_request(student_id, hours)
    print('Request created')
    
@student_cli.command('view_leaderboard', help='Displays Leaderboard')
def view_student_leaderboard():
    leaderboard = get_leaderboard()
    i = 1
    for s in leaderboard:
        student = get_student(s['id'])
        row = f"{i}: {student.firstname} {student.lastname} with {student.total_hours} hours"
        print(row)
        i+=1
        
@student_cli.command('view_accolades', help="Displays a student's accolades")
def view_student_accolades():
    print('Please enter Student ID')
    student_id = input()
    print(list_accolades(student_id))
    
app.cli.add_command(student_cli)

staff_cli = AppGroup('staff', help='Staff user commands')

@staff_cli.command("create", help="Creates a new staff member")
def create_staff_command():
    print("Enter a new username")
    username = input()
    print("Enter a password")
    password = input()
    print("Enter a new firstname")
    firstname = input()
    print("Enter a new lastname")
    lastname = input()
    create_staff(username, password, firstname, lastname)
    print("New staff member " + username + " has been created")

def list_all_requests():
    requests = list_requests()
    if requests:
        for r in requests:
            student = get_student(r.student_id)
            row = f"{r.get_json()}: {student.firstname} {student.lastname}"
            print(row)
        return True
    else:
        print("No requests waiting")
        return False
    
def list_all_students():
    students = get_all_students()
    if students:
        for s in students:
            student = get_student(s.student_id)
            row = f"{s.get_json()}: {student.firstname} {student.lastname}"
            print(row)
        return True
    else:
        print("No requests waiting")
        return False
        
@staff_cli.command('log_hours', help='Allows hours to be added to a student')
def add_hours():
    list_all_students()
    print("Please enter a student's ID")
    id = input()
    student = get_student(id)
    if student:
        print("Enter hours to be added")
        hours = input()
        student.total_hours += int(hours)
        m = f"{hours} hours was added to {student.firstname}'s total hours"
        print(m)
        add_accolade(id)
    else:
        print("Invalid ID")
        
@staff_cli.command('list_requests', help='Lists pending requests')
def list_pending_requests():
    list_all_requests()

@staff_cli.command('review_requests', help='Lists requests, allows approval or denial of requests')
def review_pending_requests():
    if list_all_requests():
        print("Enter Request ID")
        id = input()
        r = get_request(id)
        s = get_student(r.student_id)
        if r:
            print("Approve request?")
            print("Y - Yes")
            print("N - No")
            print("C - Cancel")
            option = input()
            if option == "Y":
                approve_request(id)
                add_accolade(s.id)
                m = f"Request made by {s.firstname} {s.lastname} to log {r.hours} hours was approve"
                print(m)
            elif option == "N":
                deny_request(id)
                add_accolade(s.id)
                m = f"Request made by {s.firstname} {s.lastname} to log {r.hours} hours was denied"
                print(m)
            elif option == "C":
                print("Operation cancelled")
                return
            else:
                print("Invalid option")
                return
        else:
            print("Invalid Request ID")
    else:
        print("No requests waiting")

@staff_cli.command('view_leaderboard', help='Displays Leaderboard')
def view_student_leaderboard():
    leaderboard = get_leaderboard()
    i = 1
    for s in leaderboard:
        student = get_student(s['id'])
        row = f"{i}: {student.firstname} {student.lastname} with {student.total_hours} hours"
        print(row)
        i+=1

app.cli.add_command(staff_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)