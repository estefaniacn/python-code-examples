# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Strings

my_goal = "Learn Python"

# my_goal = "I'm learning Python"
# my_goal = 'I\'m learning Python'

print(type(my_goal))

# Length

print(len(my_goal))

# Indexing

# L e a r n   P y t h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 Index

print(my_goal[0])
print(my_goal[1])
print(my_goal[2])
print(my_goal[3])

# Challenge: print the other characters.

# The last index is always len(string)-1 because 
# we start counting from 0.

# Think: what will be printed for index 5?
print(my_goal[5])

# ==================
# Example: spaces and special characters are in the grid too.

greeting = "Hello!"

# H e l l o !
# 0 1 2 3 4 5

print(greeting[5]) # !

# Negative index

print(greeting[-1])

#  H  e  l  l  o  !
# -6 -5 -4 -3 -2 -1

# Slicing

# L e a r n   P y t h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11

my_goal = "Learn Python"

print(my_goal[6:9])
print(my_goal[:5])
print(my_goal[6:])
print(my_goal[1:10:2])
print(my_goal[::-1])
