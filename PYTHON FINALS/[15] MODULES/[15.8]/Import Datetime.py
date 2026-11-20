#DATETIME MODULE
 
import datetime 
print("=== AGE CALCULATOR ===") 
birth_year = int(input("Enter your birth year:")) 
current_year = datetime.datetime.now().year 
age = current_year - birth_year 
print("Your approximate age is:", age)