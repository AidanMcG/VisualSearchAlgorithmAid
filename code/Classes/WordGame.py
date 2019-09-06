from WGSearch import WGSearch
from WGBoard import WGBoard




class WordGame(object):
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
        search = WGSearch(self.startState, self.goalState)


        if algo == "0": #bfs
            print(search.bfsSolve())
            #startTime = time.time()
            while search.openList.first().state != search.goalBoard.state:
                print (search.bfsSolve())
            #print ("--- %s seconds to complete ---" % (time.time() - startTime))
        if algo == "1": #dfs
            print (search.dfsSolve(1000))
        
        if algo == "2": #iddfs
            print(search.iddfsSolve(1))
            #return search.iddfsSolve(startBoard, goalBoard)
        
        if algo == "3": #a*
            print(search.astarSolve())
            #return search.astarSolve(startBoard, goalBoard)