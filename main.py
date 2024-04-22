import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from tetris import Tetris

import game_functions


def run_game():
	pygame.init()
	config = Settings()
	screen = pygame.display.set_mode((config.screen_width, config.screen_height))
	pygame.display.set_caption("Tetris")
	
	stats = GameStats()
	
	blocks = []
	current_tetris = Tetris(config, screen)
	# tetris_group = Group()
	
	play_button = Button(config, screen, "Play")
	play_button.rect.center = screen.get_rect().center
	play_button.msg_image_rect.center = play_button.rect.center
	
	while True:
		game_functions.check_events(config, screen, stats, blocks, play_button, current_tetris)
		if stats.game_active:
			
			if stats.tetris_controlling is False:
				game_functions.create_new_tetris(config, screen, stats, blocks, current_tetris)
			game_functions.update_tetris(config, stats, current_tetris)
			# game_functions.update_timer_event()
		game_functions.update_screen(config, screen, stats, blocks, play_button, current_tetris)


run_game()
