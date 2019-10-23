from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a Boggle grid that will hold all of the tiles for a game
    """
    return {(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)
        
    }
    
def neighbors_of_position(coords):
    """
    Get neighbors of a given position
    """
    row = coords[0]
    col = coords[1]
    
    #Assign each of the neighbors
    
    #Top-left to top-right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    #Left to right
    left = (row, col - 1)
    #The (row, col) coordinates passed to this 
    #function are here
    right = (row, col + 1)
    
    #Bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
            
def all_grid_neighbors(grid):
    """
    Get all of the possible neighbors for each position inthe grid
    """
    neighbors = {}
    for position in grid:
        position_neighbors = neighbors_of_position(position)
        neighbors[position] = [p for p in position_neighbors if p in grid]
    return neighbors
    
def path_to_word(grid, path):
    """
    Add all the letters on the path to a string
    """
    # print(grid)
    # print(path)
    return "".join([grid[p] for p in path])
    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching
    strings to words in the dictionary
    """
    neighbors = all_grid_neighbors(grid)
    paths = []
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbors[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
            
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
        
def getDictionary(dictionary_file):
    """
    Load dictionary file
    """
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]