import pygame


class Ship():
    """
    Developing a class to imitate the alien invasion ship.
    """
    def __init__(self, screen):
        """
        Initializing the ship attribute and its initial pos on the screen.
        """
        self.screen = screen

        # Load the ship image and its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
