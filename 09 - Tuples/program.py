# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Tuples

programming_languages = ("Python", "JavaScript", "C#", "Swift", "Java")

# Length

print(len(programming_languages))

# Immutable

programming_languages[1] = "Kotlin" # Error

# Indexing

# ( "Python", "JavaScript", "C#", "Swift", "Java" )
#      0           1         2       3        4

print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[2])
print(programming_languages[3])
print(programming_languages[4])

# Slicing

print(programming_languages[1:4])
print(programming_languages[1:4:2])
print(programming_languages[2:])
print(programming_languages[:4])
print(programming_languages[::2])
print(programming_languages[::-1])

# Methods

my_tuple = ("Hello", "Hello", "Hello", "World")

print(my_tuple.count("Hello"))
print(my_tuple.count("World"))

print(my_tuple.index("World"))
print(my_tuple.index("Hello"))
