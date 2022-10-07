# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: While Loops

# While Loop
x = 4

while x < 15:
    print(x)
    x += 2

# While Loops with user input
stop = False

while not stop:
    print("Hello, World!")
    answer = input("Would you like to stop? Enter Y for Yes, N for No: ")
    if answer == "Y":
        stop = True

# Infinite loop

x = 6

while x > 2:
    print(x)
    x += 2

# Press Ctrl + C or CMD + C to stop the infinite loop
