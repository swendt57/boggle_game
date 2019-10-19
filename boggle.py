
def make_grid(width, height):
    """
    Creates a Boggle grid that will hold all of the tiles for a game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
    }