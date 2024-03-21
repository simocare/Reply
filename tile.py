# classe Tile:

class Tile:
    def __init__(self, tile_id, cost, num_available, directions):
        self.tile_id = tile_id
        self.cost = cost
        self.num_available = num_available
        self.directions = directions  # A dictionary with keys 'up', 'down', 'left', 'right'

    def use_tile(self):
        if self.num_available > 0:
            self.num_available -= 1
            return True
        return False

    def linkable(self, other):
        return self.directions["up"] == other.directions["down"] or self.directions["down"] == other.directions["up"] or self.directions["left"] == other.directions["right"] or self.directions["right"] == other["left"]