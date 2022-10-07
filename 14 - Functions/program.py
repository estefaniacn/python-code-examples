# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Functions

# No parameters
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()

# One parameter
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Nora")
say_hi("Gino")

# Two parameters
def multiply(a, b):
    print(a * b)

multiply(3, 6)
multiply(8, 2)
multiply(2, 9)

# print() vs return

# With print()
def count_vowels(word):
    num_vowels = 0
    for char in word:
        if char in 'aeiou':
            num_vowels += 1
    print(num_vowels)

count_vowels("Programming")
count_vowels("Python")
count_vowels("Coding")

vowels_python = count_vowels("Python")
print(vowels_python)

# With return instead of print()
def count_vowels(word):
    num_vowels = 0
    for char in word:
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels

vowels_python = count_vowels("Python")
print(vowels_python)
