# class with 4 attributes: nord, sud, ouest, est
class Tile:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    # check if tow tiles are linkable
    def linkable(self, other):
        return self.up == other.down or self.down == other.up or self.left == other.right or self.right == other.left