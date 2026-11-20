# EASY EXAMPLES

# Example 1: greet(name)

def greet(name):
    print("Hello,", name)
greet("Andrei")


# Example 2: add(a, b)

def add(a, b):
    return a + b
result = add(10, 20)
print(result)


# Example 3: square(n)

def square(n):
    return n ** 2
print(square(5))



# INTERMEDIATE EXAMPLES

# Example 4: max_of_two(a, b)

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(15, 10))


# Example 5: is_even(n)

def is_even(n):
    return n % 2 == 0
print(is_even(10))
print(is_even(7))


# Example 6: Default Parameter

def greet_user(name="Student"):
    print("Welcome,", name)
greet_user()
greet_user("Andrei")


# HARD EXAMPLES

# Example 7: factorial(n)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))


# Example 8: Recursion - Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
