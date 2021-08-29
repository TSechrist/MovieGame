
class MovieInfo:

    def __init__(self, t, c, a):
        self.title = t
        self.clueList = c.copy()
        self.actorList = a

    def getTitle(self):
        return self.title

    def setTitle(self, t):
        self.title = t

    def getClues(self):
        return self.clueList

    def setClues(self, c):
        self.clueList = c.copy()

    def getActors(self):
        return self.actorList

    def getActorsNice(self):
        if len(self.actorList) == 1:
            return self.actorList[0]

        s = ""
        for i in range(len(self.actorList)):
            if i == len(self.actorList) - 1:
                s += "and "
            s += (self.actorList[i] + ", ")
        return s[:-2]

    def getActorsList(self):
        return self.actorList

    def setActorsList(self, a):
        self.actorList = a.copy()

    def lenActors(self):
        return len(self.actorList)

    def display(self):
        print('{} {} {}'.format(self.getTitle(), self.getClues(), self.getActors()))
