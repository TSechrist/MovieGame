
from Game import *

u = Util()


while True:
    g = Game()
    g.drawMenu()
    val = input("What would you like?: ")

    # Playing the game
    if val == "1":
        g.playGame()
        print("Your score is: " + str(g.getScore()))

    # Quitting the game
    elif val == "2":
        break


