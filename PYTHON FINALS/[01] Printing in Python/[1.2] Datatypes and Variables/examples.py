# Datatypes and Variables - Examples

#------- Easy Examples -------

# Example 1: Creating variables
print("Example 1")
name = "Raia"
age = 18
height = 1.68
print(name)
print(age)
print(height)

# Example 2: The four basic data types
print("\nExample 2")
count = 25            # int
pi = 3.14             # float
word = "Python"       # str
flag = True           # bool
print(count, pi, word, flag)

#------- Intermediate Examples -------

# Example 3: Dynamic typing - a variable can change type
print("\nExample 3")
value = 10
print(value, type(value))
value = "Ten"
print(value, type(value))
value = 10.5
print(value, type(value))

# Example 4: Type conversion with int(), float(), str()
print("\nExample 4")
print(int("42") + 8)
print(float("3.5") * 2)
print(str(100) + " points")

# Example 5: int() truncates, round() rounds
print("\nExample 5")
print(int(9.99))
print(round(9.99))
print(round(3.14159, 2))

# Example 6: bool conversion (truthy / falsy)
print("\nExample 6")
print(bool(0), bool(1))
print(bool(""), bool("hi"))
print(bool(0.0), bool(-5))

#------- Hard Examples -------

# Example 7: Rectangle area and perimeter
print("\nExample 7")
length = 8
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# Example 8: Swapping two variables using a third variable
print("\nExample 8")
a = 5
b = 10
temp = a
a = b
b = temp
print("a =", a, "b =", b)