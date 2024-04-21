import pygame
import sys
from tetris import Tetris
from block import Block


def check_keydown_events(event):
	if event.key == pygame.K_q:
		sys.exit()


def check_button(stats, play_button, mouse_x, mouse_y):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and stats.game_active is False:
		stats.game_active = True
		pygame.mouse.set_visible(False)


def check_events(stats, play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_button(stats, play_button, mouse_x, mouse_y)
		elif event.type == pygame.USEREVENT + 1:  # == tetris_auto_down_event
			# tetris_down
			if stats.tetris_controlling:
				pygame.time.set_timer(pygame.USEREVENT + 1, 1000)


def create_new_tetris(config, screen, stats, tetris_group):
	tetris = Tetris(config, screen)
	for block_pos in tetris.pattern:
		tetris.group.add(Block(tetris.config, tetris.screen, tetris.color, block_pos))
	tetris.update_pos((0, 0))
	tetris_group.add(tetris)
	
	stats.tetris_controlling = True
	

def update_tetris_group(tetris_group):
	for tetris in tetris_group.sprites():
		tetris.draw_tetris()


def draw_grid(config, screen):
	for x in range(0, config.screen_width, config.block_size):
		pygame.draw.line(screen, config.grid_color, (x, 0), (x, config.screen_height))
	for y in range(0, config.screen_height, config.block_size):
		pygame.draw.line(screen, config.grid_color, (0,y), (config.screen_width, y))


def update_screen(config, screen, stats, tetris_group, play_button):
	screen.fill(config.bg_color)
	
	if stats.game_active is False:
		draw_grid(config, screen)
		play_button.draw_button()
	else:
		update_tetris_group(tetris_group)
		draw_grid(config, screen)
	
	pygame.display.flip()
