#------- Easy Examples -------

# Example 1: Changing case
print("Example 1")
name = "juan dela cruz"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

# Example 2: strip() and len()
print("\nExample 2")
text = "   hello   "
clean = text.strip()
print(clean)
print(len(clean))

#------- Intermediate Examples -------

# Example 3: replace()
print("\nExample 3")
sentence = "I like Java"
print(sentence.replace("Java", "Python"))

# Example 4: split() and join()
print("\nExample 4")
sentence = "Python is fun to learn"
words = sentence.split()
print(words)
print(len(words))
print("-".join(words))

# Example 5: startswith(), endswith(), find()
print("\nExample 5")
email = "juan@gmail.com"
print(email.startswith("juan"))
print(email.endswith(".com"))
print(email.find("@"))

# Example 6: count() and isdigit()
print("\nExample 6")
print("banana".count("a"))
print("2026".isdigit())
print("20a6".isdigit())

#------- Hard Examples -------

# Example 7: Reverse, first/last character, palindrome
print("\nExample 7")
word = "Madam"
print(word[::-1])
print(word[0], word[-1])

clean = word.lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Example 8: Count vowels, swapcase(), spaces to underscores
print("\nExample 8")
text = "Hello World Python"

vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(count)

print(text.swapcase())
print(text.replace(" ", "_"))