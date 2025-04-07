
import sys

import pygame #This module is used to create the game window and handle events.

class AlienInvasion:

    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #Initializes the background settings that Pygame needs to run.
        #The argument is a tuple that defines the width and height of the window.
        #The window will be 1200 pixels wide and 800 pixels tall.
        #We then assign the display window to the self.screen attribute so that it will be available to other methods in the class.
        #The object assigned to self.screen is a Surface object, which represents the game window.
        #The Surface returned by display.set_mode() represents the entire game window where we can draw graphics and display images.
        self.screen = pygame.display.set_mode((1200, 800)) 
        pygame.display.set_caption("Alien Invasion") #Sets the title of the window to "Alien Invasion".

        #Set the background color of the screen to a light gray color.
        #The RGB color value (230, 230, 230) represents a light gray color.
        self.bg_color = (230, 230, 230) #This attribute will be used to fill the screen with a background color.

    def run_game(self): #This game is controlled by the run_game() method, which is the main loop of the game.
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            #The For loop is an event loop that checks for events in the game window.
            for event in pygame.event.get():# #pygame.event.get() returns a list of all the events that have occurred since the last time we checked for events.
                #The for loop iterates through each event in the list and checks if it is a QUIT event.
                if event.type == pygame.QUIT: #If the event is a QUIT event, it means the user has clicked the close button on the window.
                    #If the event is a QUIT event, we call sys.exit() to exit the program.
                    sys.exit()
                    #Redraw the screen with the background color.
                    self.screen.fill(self.bg_color)
                    #The fill() method fills the entire screen with the specified color.
            #make the most recently drawn screen visible
            pygame.display.flip() #This method updates the contents of the display window to show the most recently drawn screen.
            #The flip() method is called to update the display with the most recent changes made to the screen.
    
if __name__ == '__main__': 
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()