import unittest
from EPBoard import EPBoard, convertBoard
from EPSearch import getDepth, ep_path

class test_EPSearch(unittest.TestCase):
    def test_getDepth(self):
        current_board = EPBoard("1234b5678", 0)
        start_board = EPBoard("1234756b8", 0)
        current_board.parent = start_board
        self.assertEqual(getDepth(start_board, current_board), 1)
        
        another_board = EPBoard("1b3425678", 0)
        another_board.parent = current_board
        self.assertEqual(getDepth(start_board, another_board), 2)
    
    def test_path(self):
        current_board = EPBoard("1234b5678", 0)
        start_board = EPBoard("1234756b8", 0)
        another_board = EPBoard("1b3425678", 0)
        current_board.parent = start_board
        another_board.parent = current_board
        self.assertEqual(ep_path(start_board, another_board), [["1b3425678"], ["1234b5678"], ["1234756b8"]])