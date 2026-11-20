# Hard 7 — Using if-else in a comprehension
# The if-else expression chooses a label for every number. Unlike a filtering condition at the end, this keeps one result for each original item.
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)

# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']