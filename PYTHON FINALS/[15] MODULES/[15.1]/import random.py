# Example 1
import random

topics = ["lists", "dicts", "tuples", "sets", "functions", "exceptions"]
daily_quiz = random.sample(topics, k=3)
print("Today's topics:", daily_quiz)

# Example 2
import random

deck = ["Card A", "Card B", "Card C", "Card D"]
random.shuffle(deck)
print("Shuffled order:", deck)

# Example 3
import random

rolls = [random.randint(1, 6) for _ in range(5)]
print("5 dice rolls:", rolls)