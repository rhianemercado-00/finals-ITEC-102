"""
MODULE 13 — TUPLES, SETS & DICTIONARIES
"""

# 1. TUPLES, SETS, AND DICTIONARIES
print("\n========== 1. TUPLES, SETS, AND DICTIONARIES ==========")
# Example 1
fruits = ("Apple", "Mango", "Banana")
print("Tuple:", fruits)
# Example 2
numbers = {1, 2, 3, 4, 5}
print("Set:", numbers)
# Example 3
student = {"name": "John", "age": 20, "course": "BSIT"}
print("Dictionary:", student)


# 2. MAKE A TUPLE
print("\n========== 2. MAKE A TUPLE ==========")
# Example 1
colors = ("Red", "Blue", "Green")
print("Colors:", colors)
# Example 2
scores = (85, 90, 95, 88)
print("Scores:", scores)
# Example 3
student_info = ("Mark", 19, "BSIT", True)
print("Student information:", student_info)


# 3. TUPLE UNPACKING / SWAP
print("\n========== 3. TUPLE UNPACKING / SWAP ==========")
# Example 1
student = ("Anna", 20, "BSIT")
name, age, course = student
print("Name:", name, "| Age:", age, "| Course:", course)
# Example 2
first_number, second_number = 10, 25
first_number, second_number = second_number, first_number
print("Swapped values:", first_number, second_number)
# Example 3
scores = (90, 85, 88, 92, 95)
highest, *middle_scores, lowest = scores
print("Highest:", highest, "| Middle:", middle_scores, "| Lowest:", lowest)


# 4. UNIQUE COUNT WITH A SET
print("\n========== 4. UNIQUE COUNT WITH A SET ==========")
# Example 1
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique numbers:", set(numbers), "| Count:", len(set(numbers)))
# Example 2
names = ["John", "Mark", "John", "Anna", "Mark"]
print("Unique names:", set(names), "| Count:", len(set(names)))
# Example 3
sentence = "python is easy and python is useful"
unique_words = set(sentence.split())
print("Unique words:", unique_words, "| Count:", len(unique_words))

