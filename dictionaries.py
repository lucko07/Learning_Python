# A dictionary stores data as key : value pairs.

# Create a dictonary.
person = {
    "name": "Luckner",
    "age": 25,
    "city": "Miami"
}

print("Person dictionary:", person)

# Access value.
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Add a new key-value pair
person["job"] = "Cybersecurity "
print("Ater adding job:", person)

# Modify a value.
person["age"] = 26
print("After updating age:", person)

# Delete person city.
del person["city"]
print("After removing city:", person)

# Get all keys.
print("Keys:", person.keys())

# Get all values.
print("Values:", person.values())

# Get key-value pairs.
print("Items:", person.items())
