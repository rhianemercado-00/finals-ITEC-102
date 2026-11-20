# Intermediate 4 — Filtering even numbers
# The if condition checks whether each number has a remainder of zero when divided by 2. Only even numbers are included.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Output: [2, 4, 6, 8]