from canvasapi import Canvas 
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

# For figuring out which course is at what index
# for index, course in enumerate(all_courses):
#     if (index == 8):
#         continue
#     print(course.name + " index: " + str(index))


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

assignment = courses[1].get_assignments()[4]



print(ansh.get_missing_submissions().__sizeof__())

count = 0
for assignment in ansh.get_assignments(CS_1332):
    count += 1
print(count)