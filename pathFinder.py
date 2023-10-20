from const import *

class PathFinder:

    def __init__(self):
        self.nodes = []

    def startSearch(self,gridOb, playerCoords,targetCoords):
    
        queue = [playerCoords]

        while queue:
            x,y = queue.pop(0)

            if [x,y] == targetCoords:
                gridOb.drawNodes(x*20, y*20,TARGET)
                break

            # Left
            if x > 0 and (self.nodes[x-1][y] == EMPTY or self.nodes[x-1][y] == TARGET):
                gridOb.drawNodes((x-1)*20, y*20,QUEUE)
                queue.append((x-1,y))

            # Right 
            if x < (len(self.nodes) - 1) and (self.nodes[x+1][y] == EMPTY or self.nodes[x+1][y] == TARGET):
                gridOb.drawNodes((x+1)*20, y*20,QUEUE)
                queue.append((x+1,y))

            # Up 
            if y > 0 and (self.nodes[x][y-1] == EMPTY or self.nodes[x][y-1] == TARGET):
                gridOb.drawNodes(x*20, (y-1)*20, QUEUE)
                queue.append((x,y-1))

            # Down
            if y < (len(self.nodes[0]) - 1) and (self.nodes[x][y+1] == EMPTY or self.nodes[x][y+1] == TARGET):
                gridOb.drawNodes(x*20, (y+1)*20, QUEUE)
                queue.append((x,y+1))
