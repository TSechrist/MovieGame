from MovieInfo import MovieInfo
from MovieList import MovieList


class Util:
    # Create testing list
    def createTestList(self):

        movList = MovieList()
        movList.addMovie(MovieInfo("Moulin Rouge!", ["Fact 1", "Fact 2", "Fact 3"], ["Nicole Kidman", "Ewan McGregor", "John Leguizamo"]))
        movList.addMovie(MovieInfo("Ferris Bueller's Day Off", ["Fact 4", "Fact 5", "Fact 6"], ["Matthew Broderick", "Alan Ruck", "Mia Sara"]))
        movList.addMovie(MovieInfo("Big Fish", ["Fact 7", "Fact 8", "Fact 9"], ["Ewan McGregor", "Albert Finney", "Billy Crudup", "Jessica Lange", "Helena Bonham Carter", "Alison Lohman"]))
        movList.addMovie(MovieInfo("Moon", ["Fact 10", "Fact 11", "Fact 12"], ["Sam Rockwell"]))

        return movList

    # Sample Main Menu
    def drawMenu(self, score):
        print("*********************")
        print("----- Main Menu -----")
        print("------ 1 : Play -----")
        print("------ 2 : Exit -----")
        print("*********************")

    # Displaying details of movie
    def displayMovieFull(self, m):
        print()
        print("Movie title is: " + m.getTitle())
        print("Movie actors are: " + m.getActorsNice())
        print()
