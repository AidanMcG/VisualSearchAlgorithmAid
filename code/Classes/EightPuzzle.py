from EPSearch import EPSearch
from EPBoard import EPBoard
import sys, time


class EightPuzzle(object):
    startState = ""
    goalState = ""
    
    def __init__(self, ss, gs):
        self.startState = ss
        self.goalState = gs
    
    def getStart(self):
        return self.startState
    
    def getGoal(self):
        return self.goalState
    
    def setStart(self, ss):
        self.startState = ss
        
    def setGoal(self, gs):
        self.goalState = gs
        
    def getPath(self, algo):
        #return [x for x in range(int(self.startState), int(self.goalState))]
        
        search = EPSearch(self.startState, self.goalState)
        
        
        #print("algo is", algo)
        #print (search.dfsSolve())
        #print ()
        #algo = 0
        
        if algo == "0": #bfs
            
            startBoard = EPBoard(self.startState, 0)
            goalBoard = EPBoard(self.goalState, 0)
            
            print (startBoard.manhattan(goalBoard))
            #print(search.bfsSolve())
            startTime = time.time()
            while search.openList.first().state != search.goalBoard.state:
                print (search.bfsSolve())
            print ("--- %s seconds to complete ---" % (time.time() - startTime))
        
        if algo == "1": #dfs
            print (search.dfsSolve(1000))
        
        if algo == "2": #iddfs
            return search.iddfsSolve(1000)
        
        if algo == "3": #a*
            return search.astarSolve()
            
        