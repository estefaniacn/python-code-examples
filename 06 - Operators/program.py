# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Operators

# Arithmetic Operators

print(5 + 3)
print("Hello" + "World")
print("Hello" + " " + "World")

print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)

# Comparison Operators
# > >= < <= == !=

print(5 > 4)
print(5 >= 4)
print(5 > 5)
print(5 >= 5)
print(7 < 2)
print(2 < 2)
print(2 <= 2)
print(5 == 5)
print(5 != 3)

# Logical Operators

# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not
print(not True)
print(not False)

# Example
x = 4
y = 2

print(x > 2 and y < 2)
print(x > 2 or y < 2)

x = 6

print(not (x > 4))

# Assignment Operators

my_var = 5
print(my_var)

my_var = my_var + 2
my_var += 2
print(my_var)

my_var -= 3
print(my_var)

my_var *= 2
print(my_var)

my_var /= 4
print(my_var)

my_var **= 2
print(my_var)
