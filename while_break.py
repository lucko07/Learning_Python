# BREAK STATEMENT
# break stops a loop immediately.

while True:
    word = input("Type a word (or 'stop' to quit): ")
    if word == "stop":
        print("Loop ended.")
        break

    print("You type: ", word)