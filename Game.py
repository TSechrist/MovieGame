
from Util import *

class Game:

    def __init__(self):

        self.u = Util()
        self.score = 0
        self.round = 0
        self.maxRound = 3
        self.listOfMovies = self.u.createTestList()
        self.tempListMovies = []
        self.tMovie = self.randomMovie()


    def addScore(self, i):
        self.score = self.score + i

    def display(self):
        self.listOfMovies.display()

    def drawMenu(self):
        self.u.drawMenu(self.score)

    def randomMovie(self):
        return self.listOfMovies.random()

    # def getActorsGuess(self, input):

    def getRound(self):
        return self.round

    def getScore(self):
        return self.score

    def playGame(self):

        while (self.round < self.maxRound):
            iActorsNum = 0
            self.round += 1
            print("Round " + str(self.round) + " of " + str(self.maxRound))
            while self.tMovie in self.tempListMovies:
                self.tMovie = self.randomMovie()

            self.tempListMovies.append(self.tMovie)

            print()
            for clue in self.tMovie.getClues():
                input(clue)

            while True:

                try:
                    iActorsNum = int(input("There are " + str(self.tMovie.lenActors()) + " actors listed. How many do you "
                                                                                         "want to hear? "))

                except ValueError:
                    print("Need to enter a valid number")
                    continue

                if (iActorsNum > self.tMovie.lenActors()) or (iActorsNum < 0):
                    print("Illegal guess. Try again.")
                else:
                    break

            for i in range(self.tMovie.lenActors() - 1, self.tMovie.lenActors() - iActorsNum - 1, -1):
                input(self.tMovie.getActors()[i])

            guess = input("What movie is it?: ")
            # Check to see if movie it right
            if guess.lower() == self.tMovie.getTitle().lower():
                self.addScore(self.tMovie.lenActors() - iActorsNum)
                print("You're correct!")
            else:
                print("You're incorrect")

            print("The Movie is: " + self.tMovie.getTitle())
            print("Your current score is: " + str(self.score))
            print()
