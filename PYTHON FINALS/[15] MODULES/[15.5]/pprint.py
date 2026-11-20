# EXAMPLE 1:
import pprint

student = {
    "name": "James",
    "age": 18,
    "course": "BSIT"
}
 
#Expected output:
# {'age': 18, 'course': 'BSIT', 'name': 'James'}

pprint.pprint(student)

# EXAMPLE 2:
#import pprint

students = {
    "Student 1": {
        "name": "James",
        "grades": [90, 95, 88]
    },
    "Student 2": {
        "name": "Alex",
        "grades": [85, 89, 92]
    }
}
pprint.pprint(students)

#Expected Output:
#{'Student 1': {'grades': [90, 95, 88], 'name': 'James'},
 #'Student 2': {'grades': [85, 89, 92], 'name': 'Alex'}}


# EXAMPLE 3:
import pprint

information = {
    "name": "James",
    "subjects": ["Python", "Math", "Science"]
}

formatted = pprint.pformat(information)

print(formatted)
print(type(formatted))

#Expected Output
#{'name': 'James', 'subjects': ['Python', 'Math', 'Science']}
#<class 'str'>