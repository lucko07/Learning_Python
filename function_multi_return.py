def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

result = calculate(10, 3)

print("Result:", result)

sum_result, diff_result = calculate(10, 3)

print("Sum:", sum_result)
print("Difference:", diff_result)


# Add this function to the same file:

def get_user():
    name = "Luckner"
    age = 27
    return name, age

user_name, user_age = get_user()

print("Name:", user_name)
print("Age:", user_age)