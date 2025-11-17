# COMBINING CONDITIONS
# This is VERY common in automation and bots.

age = int(input("Enter your age: "))
has_id = input("Do you have an id? (yes / no):")

if age  >= 18 and has_id == "yes":
    print("You are allowed in.")
else:
    print("Access denied.")