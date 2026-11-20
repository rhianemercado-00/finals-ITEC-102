# Operator Precedence - Examples

#------- Easy Examples -------

# Example 1: Multiplication before addition
print("Example 1")
print(5 + 2 * 3)      # 11
print((5 + 2) * 3)    # 21

# Example 2: Same level goes left to right
print("\nExample 2")
print(10 - 4 - 2)     # 4
print(20 / 4 * 2)     # 10.0

# Example 3: Exponent before addition
print("\nExample 3")
print(2 + 3 ** 2)     # 11
print((2 + 3) ** 2)   # 25

#------- Intermediate Examples -------

# Example 4: Mixed operators
print("\nExample 4")
print(10 + 5 * 2 - 3)        # 17
print((10 + 5) * (2 - 3))    # -15

# Example 5: // and % share the same level
print("\nExample 5")
print(100 // 10 % 3)   # 1
print(7 + 8 % 3)       # 9

# Example 6: Arithmetic happens before comparison
print("\nExample 6")
print(10 > 5 + 3)      # True (10 > 8)
print(2 * 3 == 6)      # True

#------- Hard Examples -------
# Example 8: not is evaluated first
print("\nExample 7")
print(not True or True)     # True
print(not (True or True))   # False

# Example 9: Arithmetic, comparison and logical together
print("\nExample 8")
x = 5
print(x > 3 and x < 10 or x == 0)   # True
print(x + 2 > 6 and not x == 5)     # False