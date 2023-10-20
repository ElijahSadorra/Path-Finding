# Imports
import pygame as pg
import sys
from grid import GridClass
from const import  *

# Initialise pygame
pg.init()

# Class to keep game running and calling correct classes
class GameClass:
    # Constructor
    def __init__(self):
        self.screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.gameOn = True
        self.gridObject = GridClass()
        
    # Creates window view
    def createWindow(self):
        self.screen.fill(WHITE)
        self.gridObject.resetGame()
        self.gridObject.drawGrid(pg,self.screen,WINDOW_WIDTH,WINDOW_HEIGHT)

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
                    print(COOL)

            # When the buttons at the top are pressed
            elif event.type == pg.QUIT:
                self.gameOn = False
                pg.quit()
                sys.exit()

            # When the mouse is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    self.gridObject.drawMode = True

                # Draws player
                if event.button == RIGHT:
                    x, y = pg.mouse.get_pos()
                    self.gridObject.drawNodes(self.screen, x,y,PLAYER)
                
                # Draws target
                if event.button == MIDDLE:
                    x, y = pg.mouse.get_pos()
                    self.gridObject.drawNodes(self.screen, x,y,TARGET)

            if event.type == pg.MOUSEBUTTONUP:
                self.gridObject.drawMode = False
            
            if event.type == pg.MOUSEMOTION:
                
                if self.gridObject.drawMode:
                     # Gets mouse button
                    x, y = pg.mouse.get_pos()

                    # Draws nodes onto the grid
                    self.gridObject.drawNodes(self.screen,x,y,WALLS)

    # Starts main loop of system
    def start(self):
        # Main game loop activity
        while self.gameOn:
            self.event_loop()
            pg.display.flip()