# --- EASY EXAMPLES ---

# example 1: Creating a List
foods = ["Burger", "Fries", "Buldak"]
print(foods)

# example 2: Zero-based indexing
foods = ["Burger", "Fries", "Buldak"]
print(foods[0])
print(foods[1])
print(foods[2])

#  example 3: Changing vdata types
foods = ["Burger", "Fries", "Buldak"]
foods[1] = "Nuggets"
print(foods)

# example 4: Adding Element (append())
foods = ["Hatdog", "Bacon", "Ham"]
foods.append("Tocino")
print(foods)

# example 5: Removing Elements (remove())
things = ["Bag", "Pencil", "Ballpen", "Hat"]
things.remove("Bag")
print(things)

# example 6: Length of a List (len())
things = ["Bag", "Pencil", "Ballpen", "Hat"]
print(len(things))

# --- INTERMEDIATE EXAMPLE ---

# example 7 Finding the Total

numbers = [10, 6, 4, 8, 20, 40]
total = 0 

for number in numbers:
    total += number

print("Total =", total)

# example 8: Storing different data type
student = ["Nathalie", 20, True, 97.5]
print(student)
# --- Hard Example ---

# example 8: Finding the Largest in a list
n = int(input())
nums = [int(input()) for _ in range(n)]
biggest = nums[0]
for x in nums:
    if x > biggest:
        biggest = x
print(biggest)

# example 9: Finding the smallest in a list
n = int(input())
nums = [int(input()) for _ in range(n)]
smallest = nums[0]
for x  in nums:
    if x < smallest:
        smallest = x 
print(smallest)

# example 10: Display Nested Numbers

numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in numbers:
    for number in row:
        print(number, end=" ")
    print()

# Example 11: Student Grade Analyzer

students = (
    ("Anna", 95, 88),
    ("Mark", 82, 90),
    ("John", 91, 85),
    ("Lisa", 89, 94)
)

for student in students:
    name, math, science = student
    total = math + science

    print("Student:", name)
    print("Math:", math)
    print("Science:", science)
    print("Total Score:", total)
    print("----------------")