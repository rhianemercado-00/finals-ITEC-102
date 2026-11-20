# Printing in Python - Examples

#------- Easy Examples -------

# Example 1: Printing text (single or double quotes both work)
print("Example 1")
print("Hello, World!")
print('Welcome to Python Programming')

# Example 2: Printing numbers (no quotes needed)
print("\nExample 2")
print(100)
print(3.14)

# Example 3: Printing a variable
print("\nExample 3")
name = "Raia"
age = 18
print(name)
print(age)

#------- Intermediate Examples -------

# Example 4: f-string basics
print("Example 4")
name = "Raia"
score = 50
print(f"{name} scored {score} points.")

# Example 5: Expressions inside f-strings
print("\nExample 5")
a, b = 7, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

# Example 6: end= changes what print() ends with
print("\nExample 6")
print("Hello", end=" ")
print("World")

#------- Hard Examples -------

# Example 7: Receipt with variables and expressions
print("\nExample 7")
item = "Notebook"
qty = 2
price = 45
print("Item:", item)
print("Quantity:", qty)
print("Price:", price)
print("Total:", qty * price)

# Example 8: f-strings with expressions, plus sep and end
print("\nExample 8")
name = "Raia"
score1 = 50
score2 = 60
print(f"{name} scored {score1} and {score2}.")
print(f"Total: {score1 + score2}")
print(f"Average: {(score1 + score2) / 2}")
print("A", "B", "C", sep=" - ", end="!\n")