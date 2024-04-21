import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button

import game_functions


def run_game():
	pygame.init()
	config = Settings()
	screen = pygame.display.set_mode((config.screen_width, config.screen_height))
	pygame.display.set_caption("Tetris")
	
	stats = GameStats()
	
	tetris_group = Group()
	play_button = Button(config, screen, "Play")
	play_button.rect.center = screen.get_rect().center
	play_button.msg_image_rect.center = play_button.rect.center
	
	while True:
		game_functions.check_events(stats, play_button)
		game_functions.update_screen(config, screen, stats, play_button)


run_game()
