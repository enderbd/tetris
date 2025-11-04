# main window settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

# game board settings
NUM_COLS = 10
NUM_ROWS = 20
CELL_SIZE = 30
ROTATE_CD = 0.2
MOVE_DOWN_CD = 1

# tetrominos
TETROMINOS = {
    "S": {
        0: [(0, -1), (1, -1), (-1, 0), (0, 0)],
        90: [(0, 0), (0, -1), (1, 0), (1, 1)],
        180: [(0, 0), (1, 0), (-1, 1), (0, 1)],
        270: [(-1, -1), (-1, 0), (0, 0), (0, 1)],
    }
}
