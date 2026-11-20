# Hard 8 — Comparing sort() and sorted()
# This example demonstrates the key difference: sorted() creates and returns a new sorted list, while sort() rearranges the original list.
numbers = [9, 2, 7, 1, 5]

copy_sorted = sorted(numbers)
print("After sorted():", numbers)
print("New sorted list:", copy_sorted)

numbers.sort()
print("After sort():", numbers)

# Output:
# After sorted(): [9, 2, 7, 1, 5]
# New sorted list: [1, 2, 5, 7, 9]
# After sort(): [1, 2, 5, 7, 9]