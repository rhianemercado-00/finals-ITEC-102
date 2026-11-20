# Hard 7 — Using a method and functions together
# append() changes the list by adding a score. len(), max(), and sum() are built-in functions used to count, find the highest value, and calculate the total.
scores = [72, 88, 91, 65]
scores.append(95)

print("Scores:", scores)
print("Number of scores:", len(scores))
print("Highest score:", max(scores))
print("Average:", sum(scores) / len(scores))

# Output:
# Scores: [72, 88, 91, 65, 95]
# Number of scores: 5
# Highest score: 95
# Average: 82.2