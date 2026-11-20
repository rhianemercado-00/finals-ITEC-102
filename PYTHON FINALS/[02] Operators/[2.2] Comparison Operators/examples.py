# Comparison Operators - Examples

#------- Easy Examples -------

# Example 1: All six comparisons
print("\nExmaple 1")
a = 7
b = 3
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False

# Example 2: Comparing text
print("\nExample 2")
print("python" == "python")   # True
print("Python" == "python")   # False (uppercase matters)

# Example 3: Equal numbers
print("\nExample 3")
print(4 >= 4)   # True
print(4 <= 3)   # False
print(5 < 3)    # False

#------- Intermediate Examples -------

# Example 4: Saving a comparison result in a variable
print("\nExample 4")
age = 20
is_adult = age >= 18
print(is_adult)
print(type(is_adult))   # <class 'bool'>

# Example 5: Comparing calculations
print("\nExample 5")
print(2 + 3 == 5)       # True
print(10 // 3 == 3)     # True
print(10 % 2 == 0)      # True

# Example 6: Passing score check
print("\nExample 6")
score = 74
passing = 75
print("Passed:", score >= passing)   # False

#------- Hard Examples -------
# Example 7: Different types
print("\nExample 7")
print(5 == 5.0)    # True
print(5 == "5")    # False

# Example 8: Even or odd checker
print("\nExample 8")
number = 14
print(f"{number} is even: {number % 2 == 0}")
number = 7
print(f"{number} is even: {number % 2 == 0}")