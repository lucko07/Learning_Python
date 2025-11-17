# CONTINUE STATEMENT.
# continue skips the current loop iteration and goes to the next one.

"""
Skip even numbers:
"""

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)



num = 0

while num < 10:
    num += 1

    if num == 5:
        continue        # skip printing 5

    print(num)