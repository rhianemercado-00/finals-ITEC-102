# Example 1
import time

for sec in range(3, 0, -1):
  print(f"Starting in {sec}...")
  time.sleep(1)
print("Go!")

#example 2
import time

t0 = time.perf_counter()
total = sum(range(1_000_000))
elapsed = time.perf_counter() - t0
print(f"Sum={total}, took {elapsed:.4f}s")

#Example 3

import time

items = ["url_1", "url_2", "url_3"]
for item in items:
     print("Checking:", item)
     time.sleep(0.2)