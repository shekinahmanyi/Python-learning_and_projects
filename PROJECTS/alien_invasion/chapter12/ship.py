
import pygame 
class Ship:

    """A class to manage the ship."""

    def __init__(self, ai_game): #The ai_game parameter is an instance of the AlienInvasion class and is used to access the game settings and screen.

        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings #This gets the settings from the AlienInvasion class.
        self.screen_rect = ai_game.screen.get_rect() #This gets the rectangle that represents the screen dimensions.
       

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom #positioning the ship at the bottom center of the screen.

        #store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #Movement flag.
        self.moving_right = False #This is a flag that indicates whether the ship is moving to the right or not.
        self.moving_left = False #This is a flag that indicates whether the ship is moving to the left or not.
        
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's position based on the movement flags.
        #update the ship's x-coordinate based on the movement flags.
        if self.moving_right and self.rect.right < self.screen_rect.right: #This checks if the ship is moving to the right and if it is within the screen boundaries.
            #If the ship is moving to the right and is within the screen boundaries, we update its position by adding 1 to its x-coordinate.
             self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #This checks if the ship is moving to the left and if it is within the screen boundaries.
            #If the ship is moving to the left and is within the screen boundaries, we update its position by subtracting 1 from its x-coordinate.
            self.x -= self.settings.ship_speed

        #Update rect object from self.x.
        self.rect.x = self.x
    
    def blitme(self): #This draws the image to the screen at the ship's current location.
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        