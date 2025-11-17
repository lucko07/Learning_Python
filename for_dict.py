# LOOPING THROUGH A DICTIONARY.

person = {
    "name": "Luckner",
    "age": 27,
    "city": "Miami"
}

# Loop through keys.
for key in person:
    print("Key:", key)

# Loop through values.
for value in person.values():
    print("Value:", value)

# Loop through items.
for key, value in person.items():
    print(key, " ", value)
