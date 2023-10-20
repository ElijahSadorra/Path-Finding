# Imports
import pygame as pg
import sys
import math

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,255,0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

EMPTY = 0
WALLS = 1
PLAYER = 2
TARGET = 3

LEFT = 1
MIDDLE = 2
RIGHT = 3

# Initialise pygame
pg.init()

class GameObject:
    # Constructor
    def __init__(self):
        self.screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.gameOn = True
        self.nodes = []
        self.blockSize = 20
        self.drawMode = False
        self.playerDrawn = False
        self.playerCoords = []
        self.targetDrawn = False
        self.targetCoords = []
        self.pathFindAlgo = "BFS"

    # Creates window view
    def createWindow(self):
        self.screen.fill(WHITE)
        self.playerDrawn = False
        self.targetDrawn = False

        # Creates grid and append onto node array
        for x in range(0, WINDOW_WIDTH, self.blockSize):
            horizontal_node = []
            for y in range(0, WINDOW_HEIGHT, self.blockSize):
                rect = pg.Rect(x, y, self.blockSize, self.blockSize)
                horizontal_node.append(0)
                pg.draw.rect(self.screen, BLACK, rect, 1)
            self.nodes.append(horizontal_node)

    def pathFind(self):
        if self.playerDrawn and self.targetDrawn:
            if self.pathFindAlgo == "BFS":
                queue = [self.playerCoords]
               
                


    # Update node
    def drawNodes(self,x_pos, y_pos,nodeType):
        # Reduces the coordinates to the array
        x , y = math.floor(x_pos / 20) * 20 , math.floor(y_pos / 20) * 20

        # Reduces it so that it can find it in the array
        x_arr, y_arr = x // 20, y // 20

        # Draws corresponding nodes
        if nodeType == WALLS:
            rect = pg.Rect(x, y, self.blockSize, self.blockSize)
            pg.draw.rect(self.screen, RED, rect)

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
        self.nodes[x_arr][y_arr] = nodeType


    # Function which deals with all event press down
    def event_loop(self):
        for event in pg.event.get():      
            # When a key is pressed
            if event.type == pg.KEYDOWN:

                # Quits system
                if event.key == pg.K_q:
                    sys.exit()

                # Resets the board
                if event.key == pg.K_r:
                    self.createWindow()

                # Applies algorithm
                if event.key == pg.K_SPACE:
                    self.pathFind()

            # When the buttons at the top are pressed
            elif event.type == pg.QUIT:
                self.gameOn = False
                pg.quit()
                sys.exit()

            # When the mouse is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    self.drawMode = True

                # Draws player
                if event.button == RIGHT:
                    x, y = pg.mouse.get_pos()
                    self.drawNodes(x,y,PLAYER)
                
                # Draws target
                if event.button == MIDDLE:
                    x, y = pg.mouse.get_pos()
                    self.drawNodes(x,y,TARGET)

            if event.type == pg.MOUSEBUTTONUP:
                self.drawMode = False
            
            if event.type == pg.MOUSEMOTION:
                
                if self.drawMode:
                     # Gets mouse button
                    x, y = pg.mouse.get_pos()

                    # Draws nodes onto the grid
                    self.drawNodes(x,y,WALLS)

    # Starts main loop of system
    def start(self):
        # Main game loop activity
        while self.gameOn:
            self.event_loop()
            pg.display.flip()