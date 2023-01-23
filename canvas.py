from canvasapi import Canvas 
from datetime import date, timedelta
import os

API_URL = "https://gatech.instructure.com/"
API_KEY = os.environ['canvasAPIKEY']

canvas = Canvas(API_URL, API_KEY)
ansh = canvas.get_user(os.environ['canvasUserNumber'])

all_courses = ansh.get_courses(enrollment_status='active')

CS_2110 = all_courses[1]
CS_1332 = all_courses[2]
ENGL_1102 = all_courses[3]
PSYC_1101 = all_courses[6]
ISYE_3770 = all_courses[13]

courses = [CS_2110, CS_1332, ENGL_1102, PSYC_1101, ISYE_3770]

def due(utc):
    date_month_day = utc.split("T")[0][5:].split("-")
    time_hour_minute = utc.split("T")[1][:5].split(":")

    month = date_month_day[0]
    day = date_month_day[1]

    hour = time_hour_minute[0]
    if (hour[0] == "0"):
        hour = hour[1]

    minute = time_hour_minute[1]
    am_pm = ""
    day_change = False
    hour = str(int(hour) - 5)

    if (int(hour) <= 0):
        day_change = True
        hour = str(int(hour) + (23 + (int(hour) * -1)))
    if (int(hour) > 12):
        hour = str(int(hour) - 12)
        am_pm += "PM"
    else:
        am_pm += "AM"

    if (month[0] == "0"):
        month = month[1]
    if (day[0] == "0"):
        day = day[1]
    if (day_change):
        day = str(int(day) - 1)
    
    date_due = "(" + month + "/" + day + ")"
    time_due = hour + ":" + minute + " " + am_pm
    return (date_due, time_due)

def due_soon(due_date, in_days):
    due_soon_date = (date.today() + timedelta(days=in_days)).strftime("%m/%d")

    due_soon_month = due_soon_date.split("/")[0]
    due_soon_day = due_soon_date.split("/")[1]

    if (due_soon_month[0] == "0"):
        due_soon_month = due_soon_month[1]
    if (due_soon_day[0] == "0"):
        due_soon_day = due_soon_day[1]
    
    due_date = due_date[1:-1]

    due_date_month = due_date.split("/")[0]
    due_date_day = due_date.split("/")[1]

    if (due_soon_month < due_date_month):
        return False
    if (due_soon_month == due_date_month):
        return due_soon_day >= due_date_day
    return True

def passed(due_date):
    today = date.today()
    date_today = today.strftime("%m/%d")

    today_month = date_today.split("/")[0]
    today_day = date_today.split("/")[1]

    if (today_month[0] == "0"):
        today_month = today_month[1]
    if (today_day[0] == "0"):
        today_day = today_day[1]
    
    due_date = due_date[1:-1]

    due_date_month = due_date.split("/")[0]
    due_date_day = due_date.split("/")[1]

    if (today_month > due_date_month):
        return True
    if (today_month == due_date_month):
        return today_day > due_date_day
    return False

def completed():
    return False

def print_all_assignments():
    print()
    print()
    for course in courses:
        print(course.name)   
        assignments = course.get_assignments()
        print()
        print()
        print("==================================================")
        for assignment in assignments:
            if (assignment.due_at == None):
                continue
            print(assignment.name)
            print(due(assignment.due_at))
            print("==================================================")
        print()
        print()

def all_assignment_list():
    all_assignments = []
    for course in courses:
        course_assignments = []
        assignments = course.get_assignments()
        for assignment in assignments:
            if (assignment.due_at == None):
                continue
            course_assignments.append((assignment.name, due(assignment.due_at)[0], due(assignment.due_at)[1]))
        all_assignments.append(course_assignments)
    return all_assignments

def due_soon_assignment_list():
    all_assignments = []
    for course in courses:
        course_assignments = []
        assignments = course.get_assignments()
        for assignment in assignments:
            if (assignment.due_at == None):
                continue
            if (due_soon(due(assignment.due_at)[0], 7) and not passed(due(assignment.due_at)[0])): #now we need to know if I completed the assignment so something like "and not completed()"
                course_assignments.append((assignment.name, due(assignment.due_at)[0], due(assignment.due_at)[1]))
        all_assignments.append(course_assignments)
    return all_assignments

#print(due_soon_assignment_list())