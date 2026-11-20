import calendar
import string
import fractions

name = "bruce lee meow"
year = 2026
month = 11
day = 20

nice_name = string.capwords(name)
starts_capital = nice_name[0] in string.ascii_uppercase

day_number = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_number]
month_name = calendar.month_name[month]
days_in_month = calendar.monthrange(year, month)[1]
is_leap = calendar.isleap(year)

passed = fractions.Fraction(day, days_in_month)
left = fractions.Fraction(days_in_month - day, days_in_month)

print("==============================")
print("        DATE CARD")
print("==============================")
print("Name:", nice_name)
print("Starts with a capital letter:", starts_capital)
print(f"Date: {day_name}, {month_name} {day}, {year}")
print("Leap year:", is_leap)
print("Days in the month:", days_in_month)
print("Fraction of month passed:", passed)
print("Fraction of month left:", left)
print("==============================")
print(calendar.month(year, month))