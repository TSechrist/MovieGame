
from Game import *

u = Util()
g = Game()

while True and g.getRound() < 3:
    g.drawMenu()
    val = input("What would you like?: ")

    # Playing the game
    if val == "1":
        g.playGame()

    # Quitting the game
    elif val == "2":
        break

print("Your score is: " + str(g.getScore()))
