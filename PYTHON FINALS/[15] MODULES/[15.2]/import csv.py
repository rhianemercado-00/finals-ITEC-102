import csv

print("=== STUDENT RECORDS ===")
students = [
    ["Name", "Age", "Course"],
    ["Andrei", 19, "BSIT"],
    ["John", 21, "BSIT"],
    ["Mark", 22, "BSIT"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("Student records saved successfully!")