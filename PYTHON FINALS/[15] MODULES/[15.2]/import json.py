import json

print("=== STUDENT INFORMATION ===")
student = {
    "name": "Andrei",
    "age": 19,
    "course": "BSIT",
    "status": "Enrolled"
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("Student information saved successfully!")