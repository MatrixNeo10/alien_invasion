import sys

import pygame

from settings import Settings

def run_game():
    # init a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # set back color
    bg_color = ai_settings.bg_color

    # start game loop
    while True:

        # watch key and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # set background
        screen.fill(bg_color)

        # see the screen
        pygame.display.flip()


run_game()
