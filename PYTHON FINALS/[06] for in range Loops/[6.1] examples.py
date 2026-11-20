







total = 0

for number in range(2, 11, 2):
    total += number

print("Sum of even numbers:", total)





for exponent in range(0, 6):
    print(2 ** exponent)





for number in range(10, 0, -2):
    print(number)

print("Easy Challenge")
for number in range(1, 11):
    print(number)


print("Intermediate Challenge")
limit = int(input("Enter a limit: "))
for number in range(5, limit + 1, 5):
    print(number)


print("Hard Challenge")
rows = int(input("Enter the number of rows: "))
for row in range(1, rows + 1):
    for star in range(row):
        print("*", end="")
    print()





