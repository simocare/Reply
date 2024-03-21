# class with 4 attributes: nord, sud, ouest, est
class Tile:
    def __init__(self, nord, sud, ouest, est):
        self.nord = nord
        self.sud = sud
        self.ouest = ouest
        self.est = est

    # check if tow tiles are linkable
    def linkable(self, other):
        return self.nord == other.sud or self.sud == other.nord or self.ouest == other.est or self.est == other.ouest