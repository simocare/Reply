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

# search tile by id in list
def search_tile_by_id(tile_id, tiles):
    for tile in tiles:
        if tile.tile_id == tile_id:
            return tile
    return None

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

# Store the tiles in a list
tiles = [Tile_3, Tile_5, Tile_6, Tile_7, Tile_9, Tile_96, Tile_A, Tile_A5, Tile_B, Tile_C, Tile_C3, Tile_D, Tile_E, Tile_F]

# Create a WxH matrix filled with None
matrix = [["----" for _ in range(W)] for _ in range(H)]
# Populate the matrix with the golden points
for gx, gy in golden_points:
    matrix[gy][gx] = 'Gold'  # 'G' represents a golden point

# Populate the matrix with the silver points
for sx, sy, ssc in silver_points:
    matrix[sy][sx] = "S"+str(ssc)  # punteggio del silver point

# insert some tiles in the matrix
matrix[4][3] = "T3"
matrix[4][5] = "T6"
matrix[5][5] = "TC"
matrix[6][5] = "T9"
matrix[6][7] = "T96"
matrix[4][7] = "TC"
matrix[3][7] = "TC"

# Print the matrix to verify it's correct
for row in matrix:
    print(row)

# Function that given a matrix compute the score based on this rule
# the total player score is always valued on the cheapest paths
# in case of same cost, the score considers the path with minimum earned points
def check_score(matrix):
    score = 0
    # if Silver point has two tiles near by, the score icreaes by the value of the silver point
    for i in range(H):
        for j in range(W):
            if matrix[i][j][0] == "S":
                # check if there are two tiles near by
                if i-1 >= 0 and matrix[i-1][j][0] == "T" and i+1 < H and matrix[i+1][j][0] == "T":
                    score += int(matrix[i][j][1:])
                elif j-1 >= 0 and matrix[i][j-1][0] == "T" and j+1 < W and matrix[i][j+1][0] == "T":
                    score += int(matrix[i][j][1:])
    #subtract the cost of the tiles
    for i in range(H):
        for j in range(W):
            if matrix[i][j][0] == "T":
                tile = search_tile_by_id(matrix[i][j][1:], tiles)
                score -= tile.cost
    return score

# print the score
# print(check_score(matrix))

# check if all Gold are linked in pairs
# if two gold aren't linked return false
from collections import deque

def is_gold_connected(matrix, golden_points):
    # Definizione delle direzioni possibili: su, giù, sinistra, destra
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(start, goal):
        visited = set()
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current == goal:
                return True
            visited.add(current)
            for dx, dy in directions:
                next_node = (current[0] + dx, current[1] + dy)
                if 0 <= next_node[0] < len(matrix[0]) and 0 <= next_node[1] < len(matrix) and matrix[next_node[1]][next_node[0]] != "----" and next_node not in visited:
                    queue.append(next_node)
        return False

    # Verifica la connessione tra ogni coppia di punti Gold
    for i in range(len(golden_points)):
        for j in range(i + 1, len(golden_points)):
            start = golden_points[i]
            goal = golden_points[j]
            if not bfs(start, goal):
                return False
    return True

# Utilizzo della funzione per verificare la connessione dei punti Gold nella matrice
print(is_gold_connected(matrix, golden_points))

