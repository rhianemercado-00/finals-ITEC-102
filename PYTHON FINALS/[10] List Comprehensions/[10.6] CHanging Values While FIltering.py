# Intermediate 6 — Changing values while filtering
# The comprehension first checks for even numbers, then squares only the numbers that meet the condition.
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)

# Output: [4, 16, 36]