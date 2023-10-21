from const import *
import time

# A class which applies algorithm to find the shortest path
class PathFinder:
    # Constructor
    def __init__(self):
        self.nodes = []
        self.graph = {}

    # Applies search algorithm
    def startSearch(self,gridOb, playerCoords,targetCoords):
        
        queue = [playerCoords]

        while queue:
            x,y = queue.pop(0)
            
            gridOb.drawNodes(x*20, y*20,VISITED)

            # Left
            if x > 0 and (self.nodes[x-1][y][0] == EMPTY or self.nodes[x-1][y][0] == TARGET):
                gridOb.drawNodes((x-1)*20, y*20,QUEUE)
                self.nodes[x-1][y][1] = (x,y)
                queue.append((x-1,y))
                self.addToGraph(x,y,x-1,y)

            # Right 
            if x < (len(self.nodes) - 1) and (self.nodes[x+1][y][0] == EMPTY or self.nodes[x+1][y][0] == TARGET):
                gridOb.drawNodes((x+1)*20, y*20,QUEUE)
                self.nodes[x+1][y][1] = (x,y)
                queue.append((x+1,y))
                self.addToGraph(x,y,x+1,y)

            # Up 
            if y > 0 and (self.nodes[x][y-1][0] == EMPTY or self.nodes[x][y-1][0] == TARGET):
                gridOb.drawNodes(x*20, (y-1)*20, QUEUE)
                self.nodes[x][y-1][1] = (x,y)
                queue.append((x,y-1))
                self.addToGraph(x,y,x,y-1)

            # Down
            if y < (len(self.nodes[0]) - 1) and (self.nodes[x][y+1][0] == EMPTY or self.nodes[x][y+1][0] == TARGET):
                gridOb.drawNodes(x*20, (y+1)*20, QUEUE)
                self.nodes[x][y+1][1] = (x,y)
                queue.append((x,y+1))
                self.addToGraph(x,y,x,y+1)

            # If found break
            if [x,y] == targetCoords:
                gridOb.targetDrawn = False
                gridOb.drawNodes(x*20, y*20,TARGET)
                break
        
        x,y = targetCoords
        path = []
        while self.nodes[x][y][1] != 0:
            x,y = self.nodes[x][y][1]
            gridOb.drawNodes(x*20, y*20,PATH)
            path.append((x,y))
        
        gridOb.playerDrawn = False
        x,y = playerCoords
        gridOb.drawNodes(x*20, y*20,PLAYER)

    # Adds the node as a adjencency list to back track
    def addToGraph(self,x,y,newX,newY):
        arr = self.graph.get((x,y),set())
        arr.add((newX,newY))
        self.graph[(x,y)] = arr