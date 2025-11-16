# A tuple is like a list, but with one major difference:
"""
✔ Tuples cannot be changed (they are immutable)
✔ Lists can be changed

This makes tuples useful for:

data that should not be modified

coordinates

configuration values

function returns

protecting data
"""

# create a tuple.
person = ("Luckner", 27, "Miami")
print("Turple:", person)

# Access values
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])

# Lenght of turple
print("Lenght:", len(person))

# Trying to change a value (this will fail)
# person[1] = 30    # uncomment the see the error.