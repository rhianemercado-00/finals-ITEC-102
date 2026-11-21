# --- EASY EXAMPLE ---

# example 1: nested list

students = [
    ["Bogard", 90],
    ["Princess", 85],
    ["Ace", 95]
]

print(students)

# example 2 Accessing element in a nested list

students = [
    ["Bogard", 90],
    ["Princess", 85],
    ["Ace", 95]
]

print(students[0][0])
print(students[0][1])
print(students[2][0])

# example 3: Use of range()
for number in range(1, 6):
    print(number)

# --- INTERMEDIATE EXAMPLES ---

#  example 4: printing row and column

for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row {row}, Column {column}")

# example 5: creating multiplication table

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

# example 6: Altering list of lists

students = [
    ["Bogard", 90],
    ["Princess", 85],
    ["Ace", 95]
]

for student in students:
    for value in students:
        print(value)

# --- HARD EXAMPLES ---

# example 7: pattern arrangement

patterns = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"]
]

for row in patterns:
    for letter in row:
        print(letter, end=" ")
    print()

# example 8: Counting of words

words = [
    ["apple", "banana", "grape"],
    ["orange", "watermelon"],
    ["mango", "pineapple", "cherry"]
]

for group in words:
    for word in group:
        print(word, "=", len(word), "letters")
    