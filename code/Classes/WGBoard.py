import copy
import string
#import enchant


class WGBoard(object):


    DEPTH = 0
    d = {}
    datafile = open("dict.txt").read()
    datafile = datafile.split('\n')
    for line in datafile:
        d[line] = ""
    #print(d)

    def __init__(self, s, h, p=None, score=0):
        if type(s)== str:
            self.state = convertBoard(s)
        else:
            self.state = s
        self.heuristic = h
        self.parent = p
        self.score = score



    def isValidMove(self, testWord):
        #d = file(dict.txt)
        #print(self.state)
        #print(testWord)
        word = "".join(str(x) for x in self.state)
        word2 = "".join(str(y) for y in testWord)
        #print(word)
        #print(word2, "\n")
        if word != word2 and word2 in self.d:#check(word2) == True:
            #print("hit")
            return True
        else:
            return False


    def incorrectLetters(self, other):
        count = 0
        i = 0
        #print(self.state, "this is state")
        while i < len(self.state):
            if self.state[i] != other.state[i]:
                #print(self.state[i], other.state[i], "not same")
                count += 1
            #else:
                #print(self.state[i], other.state[i], "same")
            i += 1
        
        #print(i)
        #print(count,"end")
        return count




    def setParent(self, board):
        self.parent = board


    def getChildren(self):
        children = []
        alpha = list(string.ascii_lowercase)


        for i in range(len(self.state)):
            testWord = copy.deepcopy(self)
            for j in range(len(alpha)):
                testWord.state[i] = alpha[j] 
                if self.isValidMove(testWord.state):
                    hit = copy.deepcopy(testWord)
                    hit.setParent(self)
                    children.append(hit)#copying object not state




        return children






def convertBoard(s):
        board = []
        
        for letter in s:
            board += letter
        return board
