# Hard 8 — Processing names with conditions
# The condition len(name) > 5 selects names with more than five characters. title() capitalizes the first letter of each selected name.
names = ["ana", "christopher", "bea", "daniel", "alexandra"]
long_names = [name.title() for name in names if len(name) > 5]
print(long_names)

# Output: ['Christopher', 'Alexandra']