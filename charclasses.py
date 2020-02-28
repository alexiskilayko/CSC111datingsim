class Player:
    def __init__(self, name):
        self.name = name
        self.elective = []
        self.electivepartner = []
        self.club = []
        self.clubpartner = []
        self.sportsday = []
        self.dating = []

class Target:
    def __init__(self, name):
        self.name = name
        self.affection = 0

    def addpoints(self, n):
        self.affection += n

    def losepoints(self, n):
        self.affection -= n

luke = Target('Luke')
vincent = Target('Vincent')
elliot = Target('Elliot')
