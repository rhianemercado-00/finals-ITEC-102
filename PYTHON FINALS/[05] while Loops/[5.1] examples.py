




n = 5
count = 1

while count <= n:
    print(count)
    count += 1



count = 5

while count >= 1:
    print(count)
    count -= 1



n = 5
number = 1
total = 0

while number <= n:
    total += number
    number += 1

print("Sum:", total)



n = 5
number = 1
factorial = 1

while number <= n:
    factorial *= number
    number += 1

print("Factorial:", factorial)



number = 482
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)



limit = 10
number = 2

while number <= limit:
    print(number)
    number += 2



n = int(input("Enter a non-negative whole number: "))
number = 1
factorial = 1

while number <= n:
    factorial *= number
    number += 1

print("Factorial:", factorial)



number = int(input("Enter a whole number: "))
number = abs(number)
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)

print("Easy Challenge")
number = 1
while number <= 10:
    print(number)
    number += 1


print("Intermediate Challenge")
n = int(input("Enter a number: "))
number = 1
total = 0
while number <= n:
    if number % 2 != 0:
        total += number
    number += 1
print("Sum of odd numbers:", total)


print("Hard Challenge")
number = int(input("Enter a whole number: "))
number = abs(number)
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("Reversed number:", reversed_number)





