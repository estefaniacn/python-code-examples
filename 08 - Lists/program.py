# Python for Beginners
# Course by: Estefania Cassingena Navone
# Topic: Lists

favorite_games = ["Scrabble", "Monopoly", "Clue"]

# Length

print(len(favorite_games))

# Indexing

# [ "Scrabble", "Monopoly", "Clue" ]
#       0           1         2

print(favorite_games[0])
print(favorite_games[1])
print(favorite_games[2])

print(favorite_games[-1])

# Slicing

print(favorite_games[1:3])
print(favorite_games[1:])
print(favorite_games[:2])
print(favorite_games[::2])
print(favorite_games[::-1]) # Reverse

# Update elements

favorite_games[1] = "Uno"
print(favorite_games)

# Methods

favorite_games.append("Space Invaders")
print(favorite_games)

favorite_games.insert(2, "Tic-Tac-Toe")
print(favorite_games)

favorite_games.index("Monopoly")
print(favorite_games)

favorite_games.pop()
print(favorite_games)

favorite_games.remove("Scrabble")
print(favorite_games)

favorite_games.reverse()
print(favorite_games)

favorite_games.sort()
print(favorite_games)

favorite_games.clear()
print(favorite_games)
