# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Dictionaries

chemical_symbols = {
    "Hydrogen": "H",
    "Boron": "B",
    "Sodium": "Na",
    "Potassium": "K",
    "Iron": "Fe"
}

print(chemical_symbols["Hydrogen"]) # H
print(chemical_symbols["Sodium"]) # Na

# Challenge: how would you access Fe?

# Length
print(len(chemical_symbols))

# Add a key-value pair
print(chemical_symbols)
chemical_symbols["Zinc"] = "Zn" # This is a new key
print(chemical_symbols)

# Update a value
chemical_symbols["Boron"] = "Bor" # Hypothetically 
print(chemical_symbols)

# Delete a key-value pair
del chemical_symbols["Iron"]
print(chemical_symbols)

# Methods

chemical_symbols.get("Hydrogen")
print(chemical_symbols)

chemical_symbols.pop("Boron")
print(chemical_symbols)

chemical_symbols.popitem() # Remove the last-inserted key-value pair.
print(chemical_symbols)

chemical_symbols.update({"Hydrogen": "Hi", "Iron": "Ir"})
print(chemical_symbols)

chemical_symbols.clear()
print(chemical_symbols)
