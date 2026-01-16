# 🧪 Exercise 4 — Functions Calling Functions
"""
Write:

one function that adds two numbers

one function that multiplies two numbers

one function that:

uses both

adds two numbers

multiplies the result by 3
"""

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def calculate(a, b):
    sum_result = add(a, b)
    final_result = multiply(sum_result, 3)
    return final_result
 
# Call the function
result = calculate(10, 2)
print("Result:", result)