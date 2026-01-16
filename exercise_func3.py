
"""
🧪 Exercise 3 — Multiple Return Values
Write a function that:

takes a number

returns double and triple of that number
"""
def number(numb):
    double = numb * 2
    triple = numb * 3
    return double, triple

# Call the function and capture both returned values
double, triple = number(5)
print("Double: ", double)
print("Triple: ", triple)