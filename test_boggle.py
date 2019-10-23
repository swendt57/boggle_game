import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """
    Our test suite for the Boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)
    
    def test_grid_size_is_width_x_height(self):
        """
        Test toensure that the toal size of the grid 
        is equal to width * height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        """
        Test to ensure that all the coordinates inside the grid
        can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the 
        grid conatins letters
        """
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    def test_neighbors_of_a_position(self):
        """
        Ensure that a position has 8 neighbors
        """
        coords = (1, 2)
        neighbors = boggle.neighbors_of_position(coords)
        self.assertIn((0, 1), neighbors)
        self.assertIn((0, 2), neighbors)
        self.assertIn((0, 3), neighbors)
        self.assertIn((1, 1), neighbors)
        self.assertIn((1, 3), neighbors)
        self.assertIn((2, 1), neighbors)
        self.assertIn((2, 2), neighbors)
        self.assertIn((2, 3), neighbors)
        
    def test_all_grid_neighbors(self):
        """
        Ensure that all the grid positions have neighbors
        """
        grid = boggle.make_grid(2, 2)
        neighbors = boggle.all_grid_neighbors(grid)
        self.assertEqual(len(neighbors), len(grid))
        
        for position in grid:
            others = list(grid) #creates a new list from the dictionary's keys
            others.remove(position)
            self.assertListEqual(sorted(neighbors[position]), sorted(others))
            
    def test_converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid,[(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
    def test_search_grid_for_words(self):
        """
        Ensure that certain patterns can be found in a path_to_word
        """
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
    def test_load_dictionary(self):
        """
        Test that the 'get dictionary' function returns a dictionary
        that has a  length greater than 0
        """
        dictionary = boggle.getDictionary('words.txt')
        self.assertGreater(len(dictionary), 0)
        