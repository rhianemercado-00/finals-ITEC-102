from pathlib import Path

print("=== FILE ORGANIZER ===")
folder = Path("StudentRecords")
folder.mkdir(exist_ok=True)
csv_file = Path("students.csv")
json_file = Path("student.json")
print("Folder created successfully!")
if csv_file.exists():
    print("CSV file exists!")
if json_file.exists():
    print("JSON file exists!")