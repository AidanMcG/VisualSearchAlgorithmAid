import unittest
from EPBoard import EPBoard, convertBoard
from EPSearch import getDepth

class test_EPBoard(unittest.TestCase):
    def test_manhattan_distance(self):
        board1 = EPBoard("1234b5678", 0)
        board2 = EPBoard("1234756b8", 0)
        self.assertAlmostEqual(board1.manhattanDistance(board2), 1)
        board1 = EPBoard("3421b7658", 0)
        board2 = EPBoard("32b147658", 0)
        self.assertAlmostEqual(board1.manhattanDistance(board2), 2)
        board1 = EPBoard("7b2813465", 0)
        board2 = EPBoard("71286345b", 0)
        self.assertAlmostEqual(board1.manhattanDistance(board2), 3)
        
    def test_board_converter(self):
        boardString = "1234b5678"
        self.assertEqual(convertBoard(boardString), [["1","2","3"], ["4","b","5"],["6","7","8"]])
        
        boardString = "b87654321"
        self.assertEqual(convertBoard(boardString), [["b","8","7"],["6","5","4"],["3", "2","1"]])
        
        boardString = "123 456 78b"
        self.assertNotEqual(convertBoard(boardString), [["1","2","3"],["4","5","6"],["7", "8","b"]])
        


    