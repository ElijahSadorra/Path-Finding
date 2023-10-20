# Imports
import pygame as pg
import sys
from grid import GridClass
from button import Button
from buttonSwitch import ButtonSwitch
from const import  *

# Class to keep game running and calling correct classes
class GameClass:
    # Constructor
    def __init__(self):
        self.pg_init()
        self.gameOn = True
        self.gridObject = GridClass(self.screen)
    
    # Initialises pygame
    def pg_init(self):
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pg.display.set_caption("Path Finding Project")
        
    # Creates window view
    def createWindow(self):
        self.screen.fill(WHITE)
        self.gridObject.resetGame()
        self.gridObject.drawGrid(pg,WINDOW_WIDTH,abs(MENU_HEIGHT-WINDOW_HEIGHT))
        self.createButtons()

    # Creates buttons
    def createButtons(self):
        self.pathTypeButton = ButtonSwitch(BUTTON_LENGTH * 0, BUTTON_POS_X, BUTTON_LENGTH, BUTTON_HEIGHT, "Type: BFS")
        self.pathTypeButton.draw(self.screen)

        self.startButton = Button(BUTTON_LENGTH * 1, BUTTON_POS_X, BUTTON_LENGTH, BUTTON_HEIGHT, "Start Search!")
        self.startButton.draw(self.screen)

        self.resetButton = Button(BUTTON_LENGTH * 2, BUTTON_POS_X, BUTTON_LENGTH, BUTTON_HEIGHT, "Reset!")
        self.resetButton.draw(self.screen)


    # Function which deals with all event press down
    def event_loop(self):
        for event in pg.event.get():      
            # When a key is pressed
            if event.type == pg.KEYDOWN:

                # Quits system
                if event.key == pg.K_q:
                    sys.exit()

            # When the buttons at the top are pressed
            elif event.type == pg.QUIT:
                self.gameOn = False
                pg.quit()
                sys.exit()

            # When the mouse is pressed
            if event.type == pg.MOUSEBUTTONDOWN:

                # Allows draw mode to drag walls
                if event.button == LEFT:
                    self.gridObject.drawMode = True

                x, y = pg.mouse.get_pos()

                # Checks if any buttons has been pressed
                if self.pathTypeButton.clicked(x,y):
                    self.pathTypeButton.switch(self.screen)

                if self.startButton.clicked(x,y):
                    self.gridObject.startFind(self.gridObject)
            
                if self.resetButton.clicked(x,y):
                    self.createWindow()

                # Draws player
                if event.button == RIGHT and y < DRAW_AREA:
                    self.gridObject.drawNodes(x,y,PLAYER)
                
                # Draws target
                if event.button == MIDDLE and y < DRAW_AREA:
                    self.gridObject.drawNodes(x,y,TARGET)

            if event.type == pg.MOUSEBUTTONUP:
                # Removes drag click walls
                self.gridObject.drawMode = False
            
            if event.type == pg.MOUSEMOTION:
                x, y = pg.mouse.get_pos()

                if self.gridObject.drawMode and y < DRAW_AREA:
                    # Draws nodes onto the grid
                    self.gridObject.drawNodes(x,y,WALLS)

    # Starts main loop of system
    def start(self):
        self.createWindow()
        while self.gameOn:
            self.event_loop()
            pg.display.flip()

            