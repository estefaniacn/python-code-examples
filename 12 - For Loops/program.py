# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: For Loops

# For loops with range()

# One parameter
for i in range(4):
    print(i)

for i in range(4):
    print("Hello, World!")

# Two parameters
for i in range(2, 8):
    print(i)

# Three parameters
for i in range(2, 8, 2):
    print(i)

# For loops to iterate over sequences

favorite_colors = ["Blue", "Purple", "Green"]

for color in favorite_colors:
    print(color)

# For loops and dictionaries

chemical_symbols = {
    "Hydrogen": "H",
    "Boron": "B",
    "Sodium": "Na",
    "Potassium": "K",
    "Iron": "Fe"
}

for element, symbol in chemical_symbols.items():
    print(element, symbol)
