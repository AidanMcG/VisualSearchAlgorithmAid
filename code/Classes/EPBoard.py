import copy
import pygame

pygame.init()
class EPBoard(object):
    
    SMALL_INC = 25
    BIG_INC = 50
    
    def __init__(self, s, h,x=880, y=0, p=None, score=None):
        if type(s)== str:
            self.state = convertBoard(s)
        else:
            self.state = s
        self.heursitic = h
        self.parent = p
        self.score = score
        
        
        self.x=x
        if self.parent != None:
            self.y= self.parent.y + 5
        else:
            self.y = 100
        
    
    def h(self, other):
        tiles_out_of_place = 0
        i = 0
        for num in self.state:
            if num != other.state[i] and num != "b":
                tiles_out_of_place += 1
            i+=1
            
        return tiles_out_of_place
        

    def manhattanDistance(self, other):
        manhattanDistance = 0
        startManhattan = (0,0)
        goalManhattan = (0,0)
        for i in range(9):
            for y in range(3):
                for x in range(3):
                    if self.state[y][x] == str(i):
                        startManhattan = (x, y)
                        #print(startManhattan)


            for y in range(3):
                for x in range(3):
                    if other.state[y][x] == str(i):
                        goalManhattan = (x, y)
                        #print(goalManhattan)


            if startManhattan[0] >= goalManhattan[0]:
                m = startManhattan[0] - goalManhattan[0]
            else:
                m = goalManhattan[0] - startManhattan[0]


            if startManhattan[1] >= goalManhattan[1]:
                n = startManhattan[1] - goalManhattan[1]
            else:
                n = goalManhattan[1] - startManhattan[1]


            iDistance = m + n
            


            manhattanDistance = manhattanDistance + iDistance
        return manhattanDistance

        
    def f(self, other):
        return self.DEPTH + self.h(other)
    
    def getBlankPos(self):
        
        for y in range(3):
            for x in range(3):
                if self.state[y][x] == "b":
                    return (x, y)
        
    def isValidMove(self, move):
        blankx, blanky = self.getBlankPos()
        if move == "up" and blanky > 0:
            return True
        if move == "down" and blanky < 2:
            return True
        if move == "left" and blankx > 0:
            return True
        if move == "right" and blankx < 2:
            return True
        return False
        
    def setParent(self, board):
        self.parent = board
        
    def getChildren(self, small, big):
        children = []
        blankx, blanky = self.getBlankPos()
        
        
        if self.isValidMove("up"):
            uBoard = copy.deepcopy(self)
            uBoard.setParent(self)
            uBoard.state[blanky][blankx], uBoard.state[blanky-1][blankx] = uBoard.state[blanky-1][blankx], uBoard.state[blanky][blankx]
            uBoard.x = uBoard.parent.x - small
            children.append(uBoard)
            
            
        if self.isValidMove("down"):
            dBoard = copy.deepcopy(self)
            dBoard.setParent(self)
            dBoard.state[blanky][blankx], dBoard.state[blanky+1][blankx] = dBoard.state[blanky+1][blankx], dBoard.state[blanky][blankx]
            dBoard.x = dBoard.parent.x + small
            children.append(dBoard)
            
        
        if self.isValidMove("left"):
            lBoard = copy.deepcopy(self)
            lBoard.setParent(self)
            lBoard.state[blanky][blankx], lBoard.state[blanky][blankx-1] = lBoard.state[blanky][blankx-1], lBoard.state[blanky][blankx]
            lBoard.x = lBoard.parent.x - big
            children.append(lBoard)
            
            
        if self.isValidMove("right"):
            rBoard = copy.deepcopy(self)
            rBoard.setParent(self)
            rBoard.state[blanky][blankx], rBoard.state[blanky][blankx+1] = rBoard.state[blanky][blankx+1], rBoard.state[blanky][blankx]
            rBoard.x = rBoard.parent.x + big
            children.append(rBoard)
            
        self.increase()
            
        return children
    
    
    def increase(self):
    
        self.SMALL_INC += 25
        self.BIG_INC += 50
                
def convertBoard(s):
        board = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        
        i = 0
        for col in range(3):
            for row in range(3):
                board[col][row] = s[i]
                i += 1
        return board