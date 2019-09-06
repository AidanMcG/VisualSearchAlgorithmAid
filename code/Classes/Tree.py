import pygame
from pygame.locals import *

pygame.init

class Tree(object):
    
    DOWN = 5
    def __init__(self, root, rect, surf):
        self.root = root #Node
        self.rect = rect
        self.surf = surf
        self.middlex, self.middley = self.rect.midtop
        self.blitlist = []
        self.dot = pygame.image.load("dot.png")
        self.surf.blit(self.dot, [self.middlex, self.middley+10])
        
    
    def update(self, board):
        
        
        depth = self.getDepth(board)
        print (board.x)
        if board.x < 1240 and board.x > 530:
            self.surf.blit(self.dot, [board.x, 80+(depth*25)] )
        
        
    def getDepth(self, board, depth = 0):
        
        if board.state == self.root.state:
            return depth
        return self.getDepth(board.parent, depth+1)