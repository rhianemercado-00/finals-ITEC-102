# Arithmetic Operators - Examples

#------- Easy Examples -------

# Example 1: Addition, subtraction, multiplication, exponent
print("Example 1")
print(5 + 3)    # 8
print(5 - 3)    # 2
print(5 * 3)    # 15

# Example 2: Division, floor division, modulus
print("\nExample 2")
print(5 / 3)    # 1.6666666666666667
print(5 // 3)   # 1
print(5 % 3)    # 2
print(10 / 2)   # 5.0 (/ always gives a float)

# Example 3: Exponent
print("\nExample 3")
print(2 ** 3)   # 8
print(5 ** 2)   # 25
print(10 ** 0)  # 1

#------- Intermediate Examples -------

# Example 4: Even or odd using the remainder
print("\nExample 4")
print(10 % 2)   # 0 -> even
print(7 % 2)    # 1 -> odd

# Example 5: Converting minutes to hours and minutes
print("\nExample 5")
total_minutes = 135
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours, "hours and", minutes, "minutes")

#------- Hard Examples -------

# Example 6: Total bill with 12% tax\
print("\nExample 6")
price = 250
qty = 3
subtotal = price * qty
tax = subtotal * 12 // 100
total = subtotal + tax
print(f"Subtotal: {subtotal}, Tax: {tax}, Total: {total}")

# Example 7: Average of three scores
print("\nExample 7")
s1 = 90
s2 = 85
s3 = 95
average = (s1 + s2 + s3) / 3
print("Average:", average)

# Example 8: Sharing money and getting digits
print("\nExample 8")
money = 1000
people = 3
print("Each gets:", money // people)
print("Left over:", money % people)

number = 1234
print("Last digit:", number % 10)
print("Without last digit:", number // 10)