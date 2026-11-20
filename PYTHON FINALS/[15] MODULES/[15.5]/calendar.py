# EXAMPLE 1:
import calendar

print(calendar.month(2026, 11))

#Expected Output:
#   November 2026
#Mo Tu We Th Fr Sa Su
                   #1
# 2  3  4  5  6  7  8
# 9 10 11 12 13 14 15
#16 17 18 19 20 21 22
#23 24 25 26 27 28 29
#30

# EXAMPLE 2:
import calendar

year = 2024

if calendar.isleap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#Expected Output:
#2024 is a leap year.

# EXAMPLE 3:
import calendar

year = 2026
month = 11
day = 20

weekday = calendar.weekday(year, month, day)

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

print("The date falls on:", days[weekday])

#Expected Output:
#The date falls on: Friday