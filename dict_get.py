# SAFE DICTIONARY LOOKUPS USING get()
# This part is extremely important because you will use it constantly when working with

"""
APIs

JSON responses

config files

trading bots

machine learning model metadata

error-safe logic

This will prevent your programs from crashing when a key does not exist.
"""

# Solution: Use get()
# get() lets you safely access a dictionary key.
# person.get("age")

"""
✔ If the key exists → return value
✔ If the key does NOT exist → return None (or a custom default)
"""

person = {
    "name": "Luckner",
    "age": 26
}


# Normal lookup (works)
print("Name:", person["name"])


# Safe lookup with get()
print("age:", person.get("age"))


# Missing key using normal method (this crashes!)
# print(person["job"])


# Missing key using get()
print("Job:", person.get("job"))

# Provide default value
print("job (default):", person.get("job", "Not provided"))


# Another example
print("Country:", person.get("country", "Unknown"))