from MovieInfo import MovieInfo
import random

class MovieList:

    def __init__(self):
        self.listOfMovies = {}

    def getSize(self):
        return len(self.listOfMovies)

    def addMovie(self, m):
        self.listOfMovies[m.getTitle()] = m

    def display(self):
        for k, v in self.listOfMovies.items():
            print(k, ' : ', v.getClues(), ' : ', v.getActors())

    def random(self):
        return self.listOfMovies.get((random.choice(list(self.listOfMovies))))
