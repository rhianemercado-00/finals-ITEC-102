import platform
import os
import csv

# MODULE 1: PLATFORM
system_info = {
    "Operating System": platform.system(),
    "Computer Name": platform.node(),
    "Python Version": platform.python_version()
}

print("===== SYSTEM INFORMATION =====")

for key, value in system_info.items():
    print(f"{key}: {value}")

# MODULE 2: OS
folder_name = "system_reports"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file_path = os.path.join(folder_name, "system_info.csv")

# MODULE 3: CSV
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Information", "Details"])

    for key, value in system_info.items():
        writer.writerow([key, value])

print("\nSystem information saved successfully!")
print("File location:", file_path)