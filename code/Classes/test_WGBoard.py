import unittest
from WGBoard import WGBoard

class test_WGBoard(unittest.TestCase):
    def test_isValidMove(self):
        w1 = WGBoard("word", 0)
        w2 = WGBoard("lord", 0)
        self.assertTrue(w1.isValidMove(w2.state))
        w3 = WGBoard("asdf", 0)
        self.assertFalse(w1.isValidMove(w3.state))
        self.assertFalse(w1.isValidMove(w1.state))
        
    def test_incorrectLetters(self):
        w1 = WGBoard("word", 0)
        w2 = WGBoard("lord", 0)
        self.assertEqual(w1.incorrectLetters(w2), 1)
        
        w3 = WGBoard("bard", 0)
        self.assertEqual(w1.incorrectLetters(w3), 2)
        
        w1 = WGBoard("aaaaa", 0)
        w2 = WGBoard("bbbbb", 0)
        self.assertEqual(w1.incorrectLetters(w2), 5)
        
        w2 = WGBoard("aaaaa", 0)
        self.assertEqual(w1.incorrectLetters(w2), 0)