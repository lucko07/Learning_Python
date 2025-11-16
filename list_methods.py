# List methods
numbers = [5, 2, 9, 1, 7]
print("Original list:", numbers)


# Sort the list
numbers.sort()
print("Sorted list:", numbers)


# Reverse the list.
numbers.reverse()
print("Reversed list:", numbers)


# Add item to end.
numbers.append(10)
print("After append:", numbers)


# insert at a specific position.
numbers.insert(1, 100)
print("After insert:", numbers)


# Remove item by value.
numbers.remove(100)
print("After remove:", numbers)


# Pop item by index (returns it)
popped = numbers.pop(0)
print("Popped value:", popped)
print("After pop:", numbers)


# count occurrences.
numbers2 = [1, 2, 2, 3, 2, 4]
print("Count of 2:", numbers2.count(2))


# Find index of an item.
print("Index of 3:", numbers2.index(3))