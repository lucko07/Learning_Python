
# DICTIONARY UPDATES & NESTED DICTIONARIES

"""
STEP 1 — Dictionary Update Method
update() lets you modify multiple keys at once:
"""
# Simple dictionary
person = {
    "name": "Luckner",
    "age": 26
}

print("Before update:", person)


# Update multiple values
person.update({
    "age": 27,
    "city": "Miami",
    "job": "Cybersecurity"
})

print("After update:", person)


# Nested dictionary.
user = {
    "name": "Luckner",
    "contact": {
        "email": "luckner@example.com",
        "phone": "555-1234"
    },
    "address": {
        "city": "Miami",
        "state": "FL",
        "zip": 33101
    }
}

print("\nNested dictionary:", user)


# Accessing nested values
print("City:", user["address"]["city"])
print("Email:", user["contact"]["email"])


# Modify a nested value.
user["address"]["city"] = "Orlando"
print("Updated city:", user["address"]["city"])


# Add inside nested dictionary.
user["contact"]["linkedin"] = "linkedin.com/in/luckner"
print("After adding linkedin:", user["contact"])

