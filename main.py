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

# Call the function with the filename
W, H, golden_points, silver_points, tiles = read_file('00-trailer.txt')

# Print the data to verify it's correct
print(f'W: {W}, H: {H}')
print(f'Golden Points: {golden_points}')
print(f'Silver Points: {silver_points}')
print(f'Tiles: {tiles}')