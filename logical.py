# LOGICAL OPERATORS.
# Used to combine conditions.
"""
| Operator | Meaning                   | Example                         |
| -------- | ------------------------- | ------------------------------- |
| `and`    | both must be true         | `(age > 18) and (age < 65)`     |
| `or`     | at least one must be true | `(score > 90) or (score == 90)` |
| `not`    | flips true/false          | `not True → False`              |
"""

age = 25
city = "Miami"

print("Age > 18 AND city == 'Mimai': ", age > 18 and city == "Miami")
print("Age < 18 OR city == 'Miami': ", age < 18 or city == "Miami")
print("NOT(Age > 18):", not(age > 18))