
class Settings :

    """A class to store all settings for Alien Invasion."""
    
    def __init__(self) :

        """Initialize the game's static settings."""
        
        #Screen settings
        self.screen_width = 1200 #Width of the screen in pixels.
        self.screen_height = 800 #Height of the screen in pixels.
        self.bg_color = (230, 230, 230) #Background color of the screen in RGB format.

        #Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)