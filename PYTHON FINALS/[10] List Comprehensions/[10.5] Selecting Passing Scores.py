# Intermediate 5 — Selecting passing scores
# The condition includes only scores that are 75 or higher. This demonstrates filtering with a condition.
scores = [55, 82, 67, 49, 90, 73]
passing = [score for score in scores if score >= 75]
print(passing)

# Output: [82, 90]
