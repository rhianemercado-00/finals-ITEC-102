# Concatenation - Examples

#------- Easy Examples -------

# Example 1: Joining two strings with +

print("Example 1")
print("Hello" + "World")      # no space added
print("Hello" + " " + "World")

# Example 2: Concatenating string variables
print("\nExample 2")
first_name = "Bruce"
last_name = "Lee"
full_name = first_name + " " + last_name
print(full_name)

# Example 3: Variable + text
print("\nExample 3")
course = "Python Programming"
print("Welcome to " + course)

# ------ Intermediate Examples -------

# Example 4: Concatenating strings and numbers (requires type conversion)
print("\nExample 4")
age = 18
print("I am " + str(age) + " years old.")

# Example 5: Same result with 4 different methods
print("\nExample 5")
name = "Raia"
age = 18
print("Plus:   " + name + " is " + str(age))
print("Comma: ", name, "is", age)
print(f"fstring: {name} is {age}")

#------- Hard Examples -------

# Example 6: Building a full name and email
print("\nExample 6")
first, last = "juan", "delacruz"
email = first + "." + last + "@example.com"
print(email)
print(f"{first.title()} {last.title()} <{email}>")

# Example 7: Mini profile card
print("\nExample 7")
course = "Computer Engineering"
card = "Name: " + name + "\n" + "Age: " + str(age) + "\n" + "Course: " + course
print(card)

# Example 8: Build a report using +=
print("\nExample 8")
report = "SCORE REPORT\n"
report += "-" * 15 + "\n"
report += "Alice: " + str(95) + "\n"
report += "Bob:   " + str(82)
print(report)