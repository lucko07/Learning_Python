def greet(name="Guest"):
    print("Hello", name)

greet("Luckner")
greet()


# Example 3 — Multiple parameters with defaults

def calculate_price(price, tax_rate=0.05):
    total = price + (price * tax_rate)
    return total

print(calculate_price(100))
print(calculate_price(100, 0.10))