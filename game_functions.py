import pygame
import sys
from tetris import Tetris


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


def draw_grid(config, screen):
	for x in range(0, config.screen_width, config.block_size):
		pygame.draw.line(screen, config.grid_color, (x, 0), (x, config.screen_height))
	for y in range(0, config.screen_height, config.block_size):
		pygame.draw.line(screen, config.grid_color, (0,y), (config.screen_width, y))


def update_screen(config, screen, stats, play_button):
	screen.fill(config.bg_color)
	draw_grid(config, screen)
	
	if stats.game_active is False:
		play_button.draw_button()
	
	pygame.display.flip()
