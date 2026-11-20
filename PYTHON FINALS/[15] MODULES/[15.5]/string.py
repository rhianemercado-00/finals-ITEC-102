# EXAMPLE 1:
import string

print("All English Letters:")
print(string.ascii_letters)

#Expected Output:
#All English Letters:
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# EXAMPLE 2:
import string

print("Numbers:")
print(string.digits)

print("Punctuation:")
print(string.punctuation)

#Expected Output:
#Numbers:
#0123456789
#Punctuation:
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# EXAMPLE 3:
from string import Template

message = Template("Hello, $name! Welcome to $subject.")

result = message.substitute(
    name="James",
    subject="Python Programming"
)

print(result)

#Expected Output:
#Hello, James! Welcome to Python Programming.