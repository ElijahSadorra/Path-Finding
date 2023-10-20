import pygame as pg

# A class used by the gameObject to create buttons
class Button:
    # Constructor
    def __init__(self, x, y, width, height, text, color=(255, 255, 255), text_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.picture = pg.image.load("./src/imgs/button_area.png")
        self.picture = pg.transform.scale(self.picture, (self.width,self.height))
        self.font = pg.font.Font("./src/fonts/minecraft.ttf", 25)

    # Draws buttons onto the surface
    def draw(self, screen):
        # Draw the button rectangle
        screen.blit(self.picture,(self.x,self.y))

        # Draw the text on the button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        screen.blit(text_surface, text_rect)

    def clicked(self,mouseclick_x,mouseclick_y):
        return mouseclick_x >= self.x and mouseclick_x <= (self.x + self.width) and \
            mouseclick_y >= self.y and mouseclick_y <= (self.y + self.height)