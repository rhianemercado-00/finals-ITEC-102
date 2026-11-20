# Datetime Module Examples

from datetime import datetime, date, time, timedelta
import time as time_module

# Example 1: Current date and time
print("Example 1: Current Date and Time")
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Example 2: Creating specific dates
print("\nExample 2: Creating Specific Dates")
specific_date = date(2023, 12, 25)
specific_time = time(14, 30, 0)
specific_datetime = datetime(2023, 12, 25, 14, 30, 0)

print(f"Specific date: {specific_date}")
print(f"Specific time: {specific_time}")
print(f"Specific datetime: {specific_datetime}")

# Example 3: Parsing date strings
print("\nExample 3: Parsing Date Strings")
date_string = "2023-10-15 10:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date: {parsed_date}")

# Example 4: Date arithmetic
print("\nExample 4: Date Arithmetic")
today = date.today()
future_date = today + timedelta(days=30)
past_date = today - timedelta(weeks=2)

print(f"Today: {today}")
print(f"30 days from now: {future_date}")
print(f"2 weeks ago: {past_date}")

# Example 5: Calculating difference between dates
print("\nExample 5: Date Differences")
date1 = date(2023, 1, 1)
date2 = date(2023, 12, 31)
diff = date2 - date1
print(f"Days between {date1} and {date2}: {diff.days}")

# Example 6: Working with timezones (using UTC)
print("\nExample 6: UTC Time")
utc_now = datetime.utcnow()
print(f"UTC datetime: {utc_now}")

# Example 7: Formatting dates in different ways
print("\nExample 7: Date Formatting")
now = datetime.now()
formats = [
    "%Y-%m-%d",
    "%B %d, %Y",
    "%d/%m/%Y %I:%M %p",
    "%A, %B %d, %Y at %H:%M"
]

for fmt in formats:
    print(f"{fmt}: {now.strftime(fmt)}")

# Example 8: Measuring execution time
print("\nExample 8: Execution Time Measurement")
start_time = time_module.time()

# Simulate some work
sum_val = 0
for i in range(1000000):
    sum_val += i

end_time = time_module.time()
execution_time = end_time - start_time
print(f"Loop executed in {execution_time:.4f} seconds")