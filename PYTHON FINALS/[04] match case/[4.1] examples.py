#Easy 1: Basic Number Matching with case _

day = 3

match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case _:
    print("Invalid day")

# Easy 2: Matching String Commands\

command = "start"

match command:
  case "start":
    print("System starting...")
  case "stop":
    print("System stopping...")
  case "restart":
    print("System restarting...")
  case _:
    print("Unknown command")
# Easy 3: Matching Single Characters (Grades / Choices)

letter = "C"

match letter:
  case "A":
    print("Outstanding")
  case "B":
    print("Very Good")
  case "C":
    print("Satisfactory")
  case _:
    print("Unknown letter")

#Easy 4: Traffic Light Signal Matcher

signal = "green"

match signal:
  case "red":
    print("Stop")
  case "yellow":
    print("Slow down")
  case "green":
    print("Go")
  case _:
    print("Invalid signal")



#Intermediate 1: Grouping Multiple Values with | (OR Pattern)
grade = "A"

match grade:
  case "A" | "B":
    print("Excellent")
  case "C":
    print("Good")
  case "D":
    print("Needs Improvement")
  case _:
    print("Invalid grade")

#Intermediate 2: Menu Selection Program

choice = 2

match choice:
  case 1:
    print("View Profile")
  case 2:
    print("Edit Profile")
  case 3:
    print("Settings")
  case 4:
    print("Logout")
  case _:
    print("Invalid option")




#Hard: Interactive Command & Status Router

action = input("Enter command (start/stop/restart/status/exit): ").strip().lower()

match action:
  case "start" | "boot":
    print("Service status: RUNNING")
  case "restart" | "reload":
    print("Service status: RELOADING")
  case "stop" | "shutdown":
    print("Service status: STOPPED")
  case "status":
    print("Checking current service state...")
  case "exit":
    print("Closing console.")
  case _:
    print("Invalid command. Please choose a valid option.")