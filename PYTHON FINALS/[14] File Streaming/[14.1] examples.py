# File Operations in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is easy.\n")

print("File written successfully.")

# Reading entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"\nFile content:\n{content}")

# Reading file line by line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"\nAll lines as list: {lines}")

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

print("\nAfter appending:")
with open("sample.txt", "r") as file:
    print(file.read())

# Writing a list to a file
data = ["Line 1", "Line 2", "Line 3"]
with open("list_output.txt", "w") as file:
    for item in data:
        file.write(f"{item}\n")

print("\nList written to file.")

# Reading numeric data
with open("list_output.txt", "r") as file:
    numbers = []
    for line in file:
        numbers.append(line.strip())
    print(f"Read data: {numbers}")

# Exception handling with files
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

print("\nScript completed.")