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

Tile_3 = Tile("3", 10, 10, {"left": 1, "right": 1, "up": 0, "down": 0})
Tile_5 = Tile("5", 10, 10, {"left": 0, "right": 1, "up": 0, "down": 1})
Tile_6 = Tile("6", 10, 10, {"left": 1, "right": 0, "up": 0, "down": 1})
Tile_7 = Tile("7", 10, 10, {"left": 1, "right": 1, "up": 0, "down": 1})
Tile_9 = Tile("9", 10, 10, {"left": 0, "right": 1, "up": 1, "down": 0})
Tile_96 = Tile("96", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 1})
Tile_A = Tile("A", 10, 10, {"left": 1, "right": 0, "up": 1, "down": 0})
Tile_A5 = Tile("A5", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 0})
Tile_B = Tile("B", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 0})
Tile_C = Tile("C", 10, 10, {"left": 0, "right": 0, "up": 1, "down": 1})
Tile_C3 = Tile("C3", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 1})
Tile_D = Tile("D", 10, 10, {"left": 0, "right": 1, "up": 1, "down": 1})
Tile_E = Tile("E", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 1})
Tile_F = Tile("F", 10, 10, {"left": 1, "right": 1, "up": 1, "down": 1})

# Create a WxH matrix filled with None
matrix = [["----" for _ in range(W)] for _ in range(H)]
# Populate the matrix with the golden points
for gx, gy in golden_points:
    matrix[gy][gx] = 'Gold'  # 'G' represents a golden point

# Populate the matrix with the silver points
for sx, sy, ssc in silver_points:
    matrix[sy][sx] = "S"+str(ssc)  # punteggio del silver point

# Print the matrix to verify it's correct
for row in matrix:
    print(row)