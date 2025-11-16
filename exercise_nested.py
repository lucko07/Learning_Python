# Exercise 3 — Nested Dictionary 
# Build a nested dictionary named student:

student = {
    "name": "John",
    "grades": {
        "math": 90,
        "science": 85
    },
    "address": {
        "city": "Miami",
        "zip": 33101
    }
}

# Print the math grade.
print("Math grade:", student["grades"]["math"])

# Print the city
print("City:", student["address"]["city"])

# Update the science grade to 95.
student["grades"]["science"] = 95

# Add "email": "john@example.com" under "address"
student["address"]["email"] = "john@example.com"

# print the update student dictionary
print("Update tudent dictionary:", student)