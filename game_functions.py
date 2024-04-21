import pygame
import sys
import random
from tetris import Tetris
from block import Block


def check_keydown_events(stats, event, current_tetris):
	if event.key == pygame.K_q:
		sys.exit()
	elif stats.tetris_controlling is True:
		if event.key == pygame.K_RIGHT:
			current_tetris.moving_right = True
		elif event.key == pygame.K_LEFT:
			current_tetris.moving_left = True


def check_button(config, screen, stats, blocks, play_button, mouse_x, mouse_y):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and stats.game_active is False:
		stats.game_active = True
		pygame.mouse.set_visible(False)
		initialize_blocks(config, screen, blocks)


def check_events(config, screen, stats, blocks, play_button, current_tetris):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(stats, event, current_tetris)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_button(config, screen, stats, blocks, play_button, mouse_x, mouse_y)
		elif event.type == pygame.USEREVENT + 1:  # == tetris_auto_down_event
			current_tetris.moving_down = True
			stats.timer_running = False


def initialize_blocks(config, screen, blocks):
	blocks.clear()
	for row_index in range(config.screen_row):
		blocks.append([])
		for column_index in range(config.screen_column):
			blocks[-1].append(Block(config, screen, config.bg_color, (column_index, row_index)))
	return blocks


def create_new_tetris(config, screen, stats, blocks, current_tetris):
	current_tetris.group.empty()
	current_tetris.origin = [random.randint(0, int(current_tetris.config.screen_column - max([_[0] for _ in current_tetris.pattern]))), 0]
	current_tetris.update_pos(blocks, (0, 0))
	stats.tetris_controlling = True


def draw_blocks(blocks):
	for row_index in range(len(blocks)):
		for column_index in range(len(blocks[0])):
			blocks[row_index][column_index].draw_block()


def draw_grid(config, screen):
	for x in range(0, config.screen_width, config.block_size):
		pygame.draw.line(screen, config.grid_color, (x, 0), (x, config.screen_height))
	for y in range(0, config.screen_height, config.block_size):
		pygame.draw.line(screen, config.grid_color, (0, y), (config.screen_width, y))


def update_screen(config, screen, stats, blocks, play_button, current_tetris):
	screen.fill(config.bg_color)
	
	if stats.game_active is False:
		draw_grid(config, screen)
		play_button.draw_button()
	else:
		draw_blocks(blocks)
		draw_grid(config, screen)
	
	if stats.tetris_controlling:
		if stats.timer_running is False:
			stats.timer_running = True
			pygame.time.set_timer(pygame.USEREVENT + 1, config.block_moving_speed)
		
		if current_tetris.moving_left:
			current_tetris.update_pos(blocks, (-1, 0))
			current_tetris.moving_left = False
		elif current_tetris.moving_right:
			current_tetris.update_pos(blocks, (1, 0))
			current_tetris.moving_right = False
		if current_tetris.moving_down:
			current_tetris.update_pos(blocks, (0, 1))
			current_tetris.moving_down = False
	
	pygame.display.flip()
