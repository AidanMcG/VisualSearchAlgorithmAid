from WGBoard import WGBoard
from Queue import Queue
import sys, time


sys.setrecursionlimit(10000)
class WGSearch(object):
    


    def __init__(self, start, goal):
        self.startState = start
        self.goalState = goal
        self.openQueue = Queue()
        self.openList = []
        self.closedList = []
        self.frontier = []
        self.startBoard = WGBoard(self.startState, 0)
        self.goalBoard = WGBoard(self.goalState, 0)
        self.timeTaken = 0
        self.nodesExpanded = 0
        
        
        
    def bfsSolve(self):
        startTime = time.time()
        
        if self.frontier == []:
            self.frontier.append(self.startBoard.state)
        if self.openQueue.isEmpty():
            self.openQueue.enqueue(self.startBoard)
        if not self.openQueue.isEmpty():
            
            #print(self.openList.size())
            
            if self.openQueue.first().state == self.goalBoard.state:
                return self.openQueue.first().state
            #print(self.openQueue.first().state, "-------------------")
                
                
            
            children = self.openQueue.first().getChildren()
            #print(children[0].state)
        
            for child in children:
                self.nodesExpanded += 1
                if child.state not in self.closedList and child.state not in self.frontier:
                    self.frontier.append(child.state)
                    self.openQueue.enqueue(child)
                    
            self.closedList.append(self.openQueue.first().state)
            
            self.openQueue.dequeue()
        self.timeTaken = self.timeTaken + (time.time() - startTime)
            
        return self.openQueue.first().state
        
    def dfsSolve(self, maxDepth):
        if self.openList == []:
            self.openList.append(self.startBoard)
        if self.frontier == []:
            self.frontier.append(self.startBoard.state)
         
        if self.openList != []:

            if self.openList[0].state == self.goalBoard.state:
                return self.openList[0].state
            
            depth = getDepth(self.startBoard, self.openList[0])
            #print(depth)
            if depth <= maxDepth:
                children = self.openList[0].getChildren()
                listOfChildren = []
                for child in children:
                    self.nodesExpanded += 1
                    if child.state not in self.closedList and child.state not in self.frontier:
                        self.frontier.append(child.state)
                        listOfChildren.append(child)
            
                self.closedList.append(self.openList[0].state)


                self.openList = listOfChildren + self.openList[1:]


            else:
                self.closedList.append(self.openList[0].state)
                self.openList = self.openList[1:]
        if not self.openList:
            return None

        return self.openList[0].state
    
    def iddfsSolve(self, maxDepth=0):
        
        if not self.dfsSolve(maxDepth):
            result = self.dfsSolve(maxDepth)
            iddfsSolve(maxDepth+1)
            return result

    
    def astarSolve(self):
        if self.openList == []:
            self.openList.append(self.startBoard)
            depth = getDepth(self.startBoard, self.startBoard)
            lcount = self.startBoard.incorrectLetters(self.goalBoard)
            self.startBoard.score = depth + lcount

        if self.frontier == []:
            self.frontier.append(self.startBoard.state)

        if self.openList != []:
            if self.openList[0].state == self.goalBoard.state:
                return self.openList[0].state

            children = self.openList[0].getChildren()
            
            for child in children:
                self.nodesExpanded += 1

                if child.state not in self.closedList and child.state not in self.frontier:
                    depth = getDepth(self.startBoard, child)

                    lcount = child.incorrectLetters(self.goalBoard)
                    child.score = depth + lcount
                    appended = False


                    i = 0
                    for board in self.openList:
                        if child.score < board.score and appended == False and i > 0:
                            self.openList = self.openList[0:i] + [child] + self.openList[i:len(self.openList)]
                            self.frontier = self.frontier[0:i] + [child.state] + self.frontier[i:len(self.frontier)]
                            appended = True
                            break
                        i += 1

                    if appended == False:
                        self.openList.append(child)
                        self.frontier.append(child.state)

            self.closedList.append(self.openList[0])
            self.openList = self.openList[1:]

        return self.openList[0].state


    
    def getTimeTaken(self):
        return self.timeTaken
    
    def getCost(self):
        return self.cost
    
    def getNodesExpanded(self):
        return self.nodesExpanded



def getDepth(sboard, cboard):
    depth = 0
    while cboard.state != sboard.state:
        cboard = cboard.parent
        depth += 1
    return depth


"""
def getDepth(sboard, cboard, depth =0):
    
    if cboard.state == sboard.state:
        return depth
    getDepth(sboard, cboard.parent, depth+1)
"""        
    
def path(sboard, cboard, depth=0):
        if cboard.state != sboard.state:
            print ("path ",cboard.state)
            path(sboard, cboard.parent, depth+1)
            
        else:
            print ("path ", sboard.state)
            return