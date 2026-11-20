# example 1: random practice number
import random

number = random.randint(1, 20)

print("Your practice number is:", number)

# example 2: random study subject

import random

subjects = ["Programming", "Mathematics", "Networking", "English"]

chosen_subject = random.choice(subjects)

print("Study this subject:", chosen_subject)

# example 3: randomized study order
import random

tasks = ["Review notes", "Practice coding", "Answer quiz", "Read lesson"]

random.shuffle(tasks)

for task in tasks:
    print(task)