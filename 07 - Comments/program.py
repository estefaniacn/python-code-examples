# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Comments

weight = 45 # in kilograms

# This loop prints a triangle made 
# with a sequence of asterisks. 
# The triangle has five rows. 
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print("")
