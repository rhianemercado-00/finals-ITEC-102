# Easy 1 — Creating a list of squares
# The expression n ** 2 squares each number. The for part goes through every item and places the result in a new list.
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)

# Output: [1, 4, 9, 16, 25]