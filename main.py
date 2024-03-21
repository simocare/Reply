# import tile class from tile.py
from tile import Tile
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        # Read the first line and split it into individual integers
        W, H, GN, SM, TL = map(int, file.readline().split())

        # Initialize lists to store golden points, silver points, and tiles
        golden_points = []
        silver_points = []
        tiles = []

        # Read the golden points
        for _ in range(GN):
            x, y = map(int, file.readline().split())
            golden_points.append((x, y))

        # Read the silver points
        for _ in range(SM):
            x, y, score = map(int, file.readline().split())
            silver_points.append((x, y, score))

        # Read the tiles
        for _ in range(TL):
            tile_id, cost, num_available = file.readline().split()
            cost, num_available = int(cost), int(num_available)
            tiles.append((tile_id, cost, num_available))

    return W, H, golden_points, silver_points, tiles

# MAIN PROGRAM

# Call the function with the data from the file
W, H, golden_points, silver_points, tiles = read_file('00-trailer.txt')

# Print the data to verify it's correct
# print(f'W: {W}, H: {H}')
# print(f'Golden Points: {golden_points}')
# print(f'Silver Points: {silver_points}')
# print(f'Tiles: {tiles}')

# For each tile type, we need to create a Tile object and store it in a list
# Here’s a reference list indicating the directions associated with each Tile ID:
# Tile 3:
# From left to right (*)
# Tile 5:
# From down to right (*)
# Tile 6:
# From left to down (*)
# Tile 7:
# • From left to right (*)
# • From left to down (*)
# • From down to right (*)
# Tile 9:
# From up to right (*)
# Tile 96:
# • From left to down (*)
# • From up to right (*)
# Tile A:
# From left to up (*)
# Tile A5:
# • From left to up (*)
# • From down to right (*)
# Tile B:
# • From left to right (*)
# • From left to up (*)
# • From up to right (*)
# 2STANDARD EDITION
# 1
# PROBLEM STATEMENT
# Tile C:
# From up to down (*)
# Tile C3:
# • From left to right (*)
# • From up to down (*)
# Tile D:
# • From up to down (*)
# • From up to right (*)
# • From down to right (*)
# Tile E:
# • From left to up (*)
# • From left to down (*)
# • From up to down (*)
# Tile F:
# • From left to right (*)
# • From left to down (*)
# • From left to up (*)
# • From up to down (*)
# • From down to right (*)
# • From up to right (*)

Tile_3 = Tile('left', 'right', None, None)
Tile_5 = Tile(None, 'right', 'down', None)
Tile_6 = Tile('left', None, None, 'down')
Tile_7 = Tile('left', 'right', 'down', None)
Tile_9 = Tile(None, 'right', 'up', None)
Tile_96 = Tile('left', None, 'up', 'right')
Tile_A = Tile('left', None, 'up', None)
Tile_A5 = Tile('left', 'right', None, 'down')
Tile_B = Tile('left', 'right', 'up', None)
Tile_C = Tile(None, None, 'up', 'down')
Tile_C3 = Tile('left', 'right', 'up', 'down')
Tile_D = Tile(None, 'right', 'up', 'down')
Tile_E = Tile('left', 'right', 'up', 'down')
Tile_F = Tile('left', 'right', 'up', 'down')

