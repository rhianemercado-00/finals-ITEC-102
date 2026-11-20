
# Easy

#if statement
age = 19
battery_level = 85

if battery_level >= 80:
  print("Battery is well charged.")

#if-else statement

temperature_c = float(input("Enter room temperature in C: "))

if temperature_c <= 24:
  print("Room feels cool.")
else:
  print("Room feels warm.")

#if-elif-else statement

points = int(input("Enter quiz points (0-100): "))

if points >= 90:
  print("Tier A")
elif points >= 75:
  print("Tier B")
elif points >= 60:
  print("Tier C")
else:
  print("Needs Retake")

#Multiple Independent if Statements (if-if-if)
number = 15

if number > 0:
    print("Positive")

if number % 3 == 0:
    print("Divisible by 3")

if number % 5 == 0:
    print("Divisible by 5")

#Intermidiate

# Intermediate 1: Even or Odd Check (% Modulo)

number = int(input("Enter a number: "))

if number % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")

#Intermediate 2: nested if-else statement


has_ticket = input("Do you have a movie ticket? (yes/no): ").strip().lower()
viewer_age = int(input("Enter your age: "))

if has_ticket == "yes":
  if viewer_age >= 13:
    print("Enjoy the screening.")
  else:
    print("Guardian required for this film.")
else:
  print("Please purchase a ticket at the counter.")

#intermediate 3: Nested if statements
is_logged_in = True
has_permission = True

if is_logged_in:
  if has_permission:
    print("Access granted to admin settings.")



# Hard

member_status = input("Membership tier (standard/pro): ").strip().lower()
cart_total = float(input("Enter cart total: "))
coupon_applied = input("Apply promo code? (yes/no): ").strip().lower()

print("\n--- CHECKOUT SUMMARY ---")
print("Tier:", member_status)
print("Subtotal:", cart_total)

if cart_total > 0:
  if member_status == "pro" and cart_total >= 100:
    final_total = cart_total * 0.80
    print("Discount: 20% Pro Bulk")
  elif member_status == "pro" or coupon_applied == "yes":
    final_total = cart_total * 0.90
    print("Discount: 10% Standard Perk")
  else:
    final_total = cart_total
    print("Discount: None")
  print("Final Total:", round(final_total, 2))
else:
  print("Order rejected: Cart total must be greater than zero.")