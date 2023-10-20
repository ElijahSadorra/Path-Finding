from button import Button

# A child class of button which switches the text when clicking
class ButtonSwitch(Button):
    def __init__(self, x, y, width, height, text, color=(255, 255, 255), text_color=(0, 0, 0)):
        super().__init__(x, y, width, height, text, color, text_color)
        self.options = ["BFS","DFS","WALK","A*"]
    
    def switch(self,screen):
        # Queue system
        temp = self.options.pop(0)
        self.options.append(temp)

        # Change text on screen
        self.text = f"Type: {self.options[0]}"
        self.draw(screen)