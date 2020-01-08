
#Q1.
def rugby_results():
    team1 = input("Please enter the name of team one: ")
    team2 = input("Please enter the name of team two: ")
    tries_for_team1 = int(input("Please enter the number of tries for " + team1 + ":"))
    tries_for_team2 = int(input("Please enter the number of tries for " + team2 + ":"))
    points_team1 = int(input("Number of converted penalty points " + team1))
    points_team2 = int(input("Number of converted penalty points " + team2))


    print("team \t\t tries \t\t points")
    print("----------------------------------")
    print(team1, "\t\t\t", tries_for_team1, "\t\t\t", points_team1)
    print(team2, "\t\t\t", tries_for_team2, "\t\t\t", points_team2)


rugby_results()

OUTPUT
/usr/local/bin/python3.7 /Users/asahsarker/PycharmProjects/CS1117Lab2_lecture5/rugby.py
Please enter the name of team one: Japan
Please enter the name of team two: Russia
Please enter the number of tries for Japan:5
Please enter the number of tries for Russia:6
Number of converted penalty points Japan10
Number of converted penalty points Russia4
team 		 tries 		 points
----------------------------------
Japan 			 5 			 10
Russia 			 6 			 4

Process finished with exit code 0



#Q3.
def rugbyPlayerNameAndAge():
    days_in_week = 7
    rugby_name = input("Rugby Players Name: ")
    days_old = int(input("Enter no. of days old: "))
    no_of_years = int(days_old / 365)
    remaining_days = (days_old % no_of_years) % days_in_week
    print("Name: ", rugby_name, "\nYears: ", no_of_years, "\nDays: ", remaining_days)
    print(str(rugby_name )+ ' is ' + str(no_of_years) + ' years and ' + str(remaining_days )+ ' days old.')

rugbyPlayerNameAndAge()

OUTPUT
/usr/local/bin/python3.7 /Users/asahsarker/PycharmProjects/CS1117Lab2_lecture5/rugby_RUBEL.py
Rugby Players Name: Adam
Enter no. of days old: 8999
Name:  Adam
Years:  24
Days:  2
Adam is 24 years and 2 days old.


# Q4.(a)

calculating_seconds = int(42 * 60 + 42)
print("ans = " + str(calculating_seconds))

#Q4.(b)

one_mile = 1.61
km = 10
miles = int(10)/1.61
print("ans = " + str(miles))

#Q4.(c)

one_mile = 1.61
km = 10
miles = int(10)/1.61
seconds = (60) * 42 + 42
time_per_sec = (seconds / miles)
time_per_mile = (time_per_sec/60)
print("ans = " + str(time_per_mile))






#Q6.
departure_time_hours = 6
departure_time_minutes = 52
departure_time_seconds = (departure_time_hours * 3600) + (departure_time_minutes * 60)


easy_pace_mins = 8
easy_pace_secs = 15
easy_pace_total_sec = (easy_pace_mins * 60) + easy_pace_secs

faster_pace_mins = 7
faster_pace_secs = 12
faster_pace_total_sec = (faster_pace_mins * 60) + faster_pace_secs

time_spent_running = (easy_pace_total_sec * 2) + (faster_pace_total_sec * 3)
time_return_home_total_secs = departure_time_seconds + time_spent_running

time_return_home_hours = time_return_home_total_secs // 3600
time_return_home_mins = (time_return_home_total_secs % 3600) // 60
time_return_home_secs = (time_return_home_mins % 3600) % 60
print(time_return_home_hours, ":",
time_return_home_mins, ":", time_return_home_secs, "(HH:MM:SS)")


OUTPUT
/usr/local/bin/python3.7 /Users/asahsarker/PycharmProjects/CS1117Lab2_lecture5/bugs.py
7 : 30 : 30 (HH:MM:SS)
