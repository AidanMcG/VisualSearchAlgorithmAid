from EightPuzzle import EightPuzzle
import sys

def main():
    start = sys.argv[1]
    goal = sys.argv[2]
    puzzleOption = sys.argv[3]
    algoOption = sys.argv[4]
    
    try:
        assert len(start) == 9
    except AssertionError as e:
        e.args += ("Youre", "wrong!")
        raise
        
    try:
        assert len(goal) == 9
    except AssertionError as e:
        e.args += ("Youre", "wrong!")
        raise
        
    if puzzleOption == "0": #eightpuzzle
        ep = EightPuzzle(start, goal)
        ep.getPath(algoOption)

    if puzzleOption == "1": #wordgame
        wg = WordGame(start, goal)
        wg.getPath(algoOption)
        
    
    
if __name__ == "__main__":
    main()