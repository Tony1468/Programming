"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
 
Explanation video: http://youtu.be/BCxWJgN4Nnc
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame as pg
 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pg.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
           # Load the player image
        self.image = pg.image.load("player_image.png").convert()
        # Optional: You may want to scale the image to match the desired dimensions
        self.image = pg.transform.scale(self.image, (40, 60))

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    # Other methods remain unchanged


class CustomLevel(Level):
    """ Definition for a custom level. """

    def __init__(self, player):
        """ Create a custom level. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Define the platforms for this level
        level = [
            [210, 70, 500, 500],
            [210, 70, 200, 400],
            [210, 70, 600, 300],
            # Add new platforms below
            [100, 30, 100, 200],  # Example of a new platform
            # Define more platforms as needed
        ]

        # Add platforms to the level
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

# Then, in the start() function, instead of Level_01, use CustomLevel:
# level_list.append(CustomLevel(player))