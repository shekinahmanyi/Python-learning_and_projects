
import sys

import pygame #This module is used to create the game window and handle events.

from settings import Settings #Import the Settings class from the settings module.
from ship import Ship #Import the Ship class from the ship module.
class AlienInvasion:

    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #Initializes the background settings that Pygame needs to run.
        #The argument is a tuple that defines the width and height of the window.
        #We then assign the display window to the self.screen attribute so that it will be available to other methods in the class.
        #The object assigned to self.screen is a Surface object, which represents the game window.
        #The Surface returned by display.set_mode() represents the entire game window where we can draw graphics and display images.
        self.settings = Settings() 
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) #This settings comes from the Settings class.
        pygame.display.set_caption("Alien Invasion") #Sets the title of the window to "Alien Invasion".
        
        self.ship = Ship(self) #Creates an instance of the Ship class and assigns it to the self.ship attribute.

    def run_game(self): #This game is controlled by the run_game() method, which is the main loop of the game.
        """Start the main loop for the game."""
        while True:
            self._check_events() #This is also known as the helper method and is called to check for events in the game window.
            self.ship.update() #This method is called to update the ship's position based on the movement flags.
            #The update() method is called to update the ship's position based on the movement flags.
            self._update_screen() #This is also known as the helper method and is called to update the screen with the most recent changes made to it.
                    #Redraw the screen with the background color.
           
    def _check_events(self):
        #The For loop is an event loop that checks for events in the game window.
        for event in pygame.event.get():# #pygame.event.get() returns a list of all the events that have occurred since the last time we checked for events.
        #The for loop iterates through each event in the list and checks if it is a QUIT event.
            if event.type == pygame.QUIT: #If the event is a QUIT event, it means the user has clicked the close button on the window.
            #If the event is a QUIT event, we call sys.exit() to exit the program.
                sys.exit()
            elif event.type == pygame.KEYDOWN: #If the event is a KEYDOWN event, it means the user has pressed a key on the keyboard.
                if event.key == pygame.K_RIGHT: #If the key pressed is 'q', we call sys.exit() to exit the program.
                    #move the ship to the right when the 'q' key is pressed.
                    self.ship.moving_right = True #This sets the moving_right attribute of the ship to True, indicating that the ship should move to the right.
            elif event.type == pygame.KEYUP: #If the event is a KEYUP event, it means the user has released a key on the keyboard.
                if event.key == pygame.K_RIGHT: #If the key released is 'q', we call sys.exit() to exit the program.
                    #stop the ship when the 'q' key is released.
                    self.ship.moving_right = False


    def _update_screen(self):

        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color) #comes from the Settings class.
                    #The fill() method fills the entire screen with the specified color.
        self.ship.blitme()
                    #The blitme() method draws the ship at its current location on the screen.
            #make the most recently drawn screen visible
            #The flip() method updates the contents of the display window to show the most recently drawn screen.
        pygame.display.flip() #This method is called to update the display window with the most recent changes made to it.
    
if __name__ == '__main__': 
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()