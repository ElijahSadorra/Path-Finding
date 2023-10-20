import pygame as pg
import math
from const import  *
from pathFinder import PathFinder

# Class to create and manage nodes on the screen
class GridClass:
    # Constructor
    def __init__(self,screen):
        self.pathFind = PathFinder()
        self.screen = screen
        self.blockSize = 20
        self.drawMode = False
        self.playerDrawn = False
        self.playerCoords = []
        self.targetDrawn = False
        self.targetCoords = []

    # Resets to default valuess
    def resetGame(self):
        self.pathFind.nodes = []
        self.playerDrawn = False
        self.playerCoords = []
        self.targetDrawn = False
        self.targetCoords = []

    # Draw the grid onto the screen
    def drawGrid(self,pg,width,height):
        # Creates grid and append onto node array
        for x in range(0, width, self.blockSize):
            horizontal_node = []
            for y in range(0, height, self.blockSize):
                rect = pg.Rect(x, y, self.blockSize, self.blockSize)
                horizontal_node.append(0)
                pg.draw.rect(self.screen, BLACK, rect, 1)
            self.pathFind.nodes.append(horizontal_node)

     # Update nodes
    def drawNodes(self,x_pos, y_pos,nodeType):
        # Reduces the coordinates to the array
        x , y = math.floor(x_pos / 20) * 20 , math.floor(y_pos / 20) * 20

        # Reduces it so that it can find it in the array
        x_arr, y_arr = x // 20, y // 20

        # Draws corresponding nodes
        if nodeType == WALLS and self.pathFind.nodes[x_arr][y_arr] == EMPTY:
            rect = pg.Rect(x, y, self.blockSize, self.blockSize)
            pg.draw.rect(self.screen, RED, rect)

        elif nodeType == QUEUE: 
            rect = pg.Rect(x, y, self.blockSize, self.blockSize)
            pg.draw.rect(self.screen, PURPLE, rect)

        elif nodeType == PLAYER and self.playerDrawn == False:
            rect = pg.Rect(x, y, self.blockSize, self.blockSize)
            pg.draw.rect(self.screen, BLUE, rect)
            self.playerDrawn = True
            self.playerCoords = [x_arr,y_arr]

        elif nodeType == TARGET and self.targetDrawn == False:
            rect = pg.Rect(x, y, self.blockSize, self.blockSize)
            pg.draw.rect(self.screen, GREEN, rect)
            self.targetDrawn = True
            self.targetCoords = [x_arr,y_arr]

        # Updates the node values
        self.pathFind.nodes[x_arr][y_arr] = nodeType
        pg.display.flip()
        

    # Starts path-find algo
    def startFind(self,gridOb):
        self.pathFind.startSearch(gridOb,self.playerCoords,self.targetCoords)