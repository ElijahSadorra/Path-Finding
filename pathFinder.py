from const import *
import random

# A class which applies algorithm to find the shortest path
class PathFinder:
    # Constructor
    def __init__(self):
        self.nodes = []
        self.graph = {}
        self.type = "BFS"
        self.options = ["DFS","WALK","A*","BFS"]

    def startFind(self,gridOb, playerCoords,targetCoords):
        if self.type == "BFS":
            self.startBFS(gridOb, playerCoords,targetCoords)
        elif self.type == "DFS":
            self.startDFS(gridOb, playerCoords,targetCoords)

    def reset(self):
        self.nodes = []
        self.graph = {}
        self.type = "BFS"
        self.options = ["DFS","WALK","A*","BFS"]

    # Applies search algorithm
    def startBFS(self,gridOb, playerCoords,targetCoords):
        
        queue = [playerCoords]
        while queue:
            x,y = queue.pop(0)
            
            gridOb.drawNodes(x*20, y*20,VISITED)
            neighbour = self.findNeighbors(gridOb,x,y,targetCoords)

            if neighbour == FOUND:
                break
            
            queue += neighbour


        self.findPath(gridOb,playerCoords,targetCoords)

    # Applies search algorithm
    def startDFS(self,gridOb, playerCoords,targetCoords):
        
        stack = [playerCoords]
        while stack:
            x,y = stack[-1]
            
            gridOb.drawNodes(x*20, y*20,VISITED)

            neighbour = self.findNeighbors(gridOb,x,y,targetCoords)

            if neighbour == FOUND:
                break

            if len(neighbour) == 0:
                x,y = stack.pop()
                gridOb.drawNodes(x*20, y*20,BACKTRACK)
            else:
                stack += neighbour

        self.findPath(gridOb,playerCoords,targetCoords)

    def findNeighbors(self,gridOb,x,y,targetCoords):
            arr = []

            # Left
            if x > 0 and (self.nodes[x-1][y][0] == EMPTY or self.nodes[x-1][y][0] == TARGET):
                gridOb.drawNodes((x-1)*20, y*20,QUEUE)
                self.nodes[x-1][y][1] = (x,y)
                arr.append((x-1,y))

            # Right 
            if x < (len(self.nodes) - 1) and (self.nodes[x+1][y][0] == EMPTY or self.nodes[x+1][y][0] == TARGET):
                gridOb.drawNodes((x+1)*20, y*20,QUEUE)
                self.nodes[x+1][y][1] = (x,y)
                arr.append((x+1,y))

            # Up 
            if y > 0 and (self.nodes[x][y-1][0] == EMPTY or self.nodes[x][y-1][0] == TARGET):
                gridOb.drawNodes(x*20, (y-1)*20, QUEUE)
                self.nodes[x][y-1][1] = (x,y)
                arr.append((x,y-1))

            # Down
            if y < (len(self.nodes[0]) - 1) and (self.nodes[x][y+1][0] == EMPTY or self.nodes[x][y+1][0] == TARGET):
                gridOb.drawNodes(x*20, (y+1)*20, QUEUE)
                self.nodes[x][y+1][1] = (x,y)
                arr.append((x,y+1))

            # If found break
            if [x,y] == targetCoords:
                gridOb.targetDrawn = False
                gridOb.drawNodes(x*20, y*20,TARGET)
                return FOUND
        
            return arr

    # Finds the path back
    def findPath(self,gridOb,playerCoords,targetCoords):

        x,y = targetCoords
        path = []
        while self.nodes[x][y][1] != 0:
            x,y = self.nodes[x][y][1]
            gridOb.drawNodes(x*20, y*20,PATH)
            path.append((x,y))
        
        gridOb.playerDrawn = False
        x,y = playerCoords
        gridOb.drawNodes(x*20, y*20,PLAYER)


    def switch(self):
        self.type = self.options.pop(0)
        self.options.append(self.type)
