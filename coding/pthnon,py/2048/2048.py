import curses
import random
import numpy as np

BOARDSIZE = 4
board = np.zeros((BOARDSIZE, BOARDSIZE), np.int16)

keys = {
    'a': 0,
    'w': 1,
    'd': 2,
    's': 3
}

# Define the RGB colors based on the provided Java color codes
color_pairs_rgb = {
    0: (204, 192, 179),    # Empty tile
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    'other': (0, 0, 0)      # Tiles beyond 2048 (default black background)
}


def rgb_to_curses(rgb_tuple):
    """Convert RGB values (0-255) to curses color scale (0-1000)"""
    return tuple(int(x * 1000 / 255) for x in rgb_tuple)


def init_colors():
    """Initialize colors in curses"""
    curses.start_color()
    # Initialize each color pair from the RGB dictionary
    for i, (key, rgb) in enumerate(color_pairs_rgb.items(), start=1):
        r, g, b = rgb_to_curses(rgb)
        curses.init_color(i, r, g, b)  # Initialize color
        curses.init_pair(i, curses.COLOR_BLACK, i)  # Black text, background color


def drawgrid(screen,score):
    """Draw the grid with 5x5 colored tiles"""
    tile_width = 11  # Increased width for wider tiles
    tile_height = 5  # Tile height remains the same

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            # Fetch color pair, default to 'other' (black background) if tile number not found
            color_pair = curses.color_pair(
                list(color_pairs_rgb.keys()).index(num) + 1 if num in color_pairs_rgb else len(color_pairs_rgb)
            )

            # Center the number in the middle of the tile
            tile = [" " * tile_width] * tile_height
            if num != 0:
                num_str = str(num)
                centered_num = num_str.center(tile_width)
                tile[tile_height // 2] = centered_num  # Center the number on the middle row

            # Draw the entire 5x5 tile with the background color
            for k in range(tile_height):
                screen.addstr(i * tile_height + k, j * tile_width, tile[k], color_pair)
    screen.addstr("SCORE: "+str(score))

def keypress(screen):
    key = 'q'
    while key not in keys:
        key = screen.getkey()
    return key

def leftify(row):
    for i in range(0, len(row)):
        for j in range(i, len(row)):
            if row[j] != 0 and row[i] == 0:
                row[i] = row[j]
                row[j] = 0
                break

def combine(row,score):
    for i in range(0, len(row)):
        for j in range(i + 1, len(row)):
            if row[j] == row[i]:
                row[i] *= 2
                row[j] = 0
                score+=row[i]
                break

def tilemove(key, board,score):
    rotations = keys[key]
    board = np.rot90(board, rotations)  # Rotate the board
    for row in board:
        combine(row,score)
        leftify(row)
    board = np.rot90(board, 4 - rotations)  # Rotate the board back

def addtiles(board):
    for _ in range(2):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if np.all(board==0):
            while board[row][col] != 0:
                row = random.randint(0, 3)
                col = random.randint(0, 3)
            num = random.randint(0, 9)
            board[row][col] = 4 if num == 1 else 2  # 10% chance of a 4, 90% chance of a 2

def game(screen):
    score=0
    curses.noecho()
    curses.cbreak()

    init_colors()  # Initialize colors
    running = True
    addtiles(board)
    while running:
        screen.clear()
        drawgrid(screen,score)
        tilemove(keypress(screen), board,score)
        addtiles(board)

# Start the game
curses.wrapper(game)
