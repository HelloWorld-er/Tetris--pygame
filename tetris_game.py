import os
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from tetris import Tetris

import game_functions


def run_game(config, stats, scoreboard_window, user_board_window, x=0, y=0):
	scoreboard_window.username = user_board_window.username
	os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
	
	pygame.init()
	
	screen = pygame.display.set_mode((config.play_screen_width, config.play_screen_height))
	pygame.display.set_caption("Tetris")
	
	blocks = []
	current_tetris = Tetris(config, screen, stats)
	
	play_button = Button(config, screen, "Play")
	play_button.rect.center = screen.get_rect().center
	# play_button.rect.x -= int((config.screen_width - config.play_screen_width) / 2)
	play_button.msg_image_rect.center = play_button.rect.center
	
	# scoreboard = ScoreBoard(config, screen)
	
	while True:
		game_functions.check_events(config, screen, stats, scoreboard_window, blocks, play_button, current_tetris)
		if stats.game_active:
			if stats.tetris_controlling is False:
				game_functions.initialize_new_term(config, screen, stats, blocks, current_tetris)
			game_functions.update_tetris(config, stats, blocks, current_tetris)
		game_functions.update_screen(config, screen, stats, blocks, play_button, current_tetris)
