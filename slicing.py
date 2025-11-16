# Slicing
# Slicing allows you to extract parts of a list.
# Think of a slice as: [start : end]

"""
start = index where slice begins
end = index where slice stops (but NOT included)
"""
numbers = [10, 20, 30, 40, 50, 60]
print("All numbers:", numbers)

# Slice examples
print("First three:", numbers[0:3])
print("Middle two:", numbers[2:4])
print("Last three:", numbers[-3:])
print("Last three:", numbers[3:6])


# Shortcuts
print("From start to index 3:", numbers[:3])
print("From index 2 to end:", numbers[2:])
print("Whole list:", numbers[:])
