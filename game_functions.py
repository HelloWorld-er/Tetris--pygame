import pygame
import sys
from block import Block


def check_keydown_events(stats, event, current_tetris):
	if event.key == pygame.K_q:
		sys.exit()
	elif stats.tetris_controlling:
		if event.key == pygame.K_RIGHT:
			current_tetris.moving_right = True
		elif event.key == pygame.K_LEFT:
			current_tetris.moving_left = True
		elif event.key == pygame.K_UP:
			current_tetris.rotate_tetris = True


def check_keyup_events(stats, event, current_tetris):
		if stats.tetris_controlling:
			if event.key == pygame.K_RIGHT:
				current_tetris.moving_right = False
			elif event.key == pygame.K_LEFT:
				current_tetris.moving_left = False
			elif event.key == pygame.K_UP:
				current_tetris.rotate_tetris = False


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
		elif event.type == pygame.KEYUP:
			check_keyup_events(stats, event, current_tetris)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_button(config, screen, stats, blocks, play_button, mouse_x, mouse_y)
		elif stats.tetris_controlling and event.type == pygame.USEREVENT + 1:
			stats.manual_timer_running = False
		elif stats.tetris_controlling and event.type == pygame.USEREVENT + 2:
			stats.rotate_timer_running = False
		elif stats.tetris_controlling and event.type == pygame.USEREVENT + 3:
			current_tetris.moving_down = True
			stats.auto_timer_running = False


def initialize_blocks(config, screen, blocks):
	blocks.clear()
	for row_index in range(config.screen_row):
		blocks.append([])
		for column_index in range(config.screen_column):
			blocks[-1].append(Block(config, screen, config.bg_color, (column_index, row_index)))
	return blocks


def initialize_new_term(config, screen, stats, blocks, current_tetris):
	current_tetris.initialize_tetris(blocks)
	stats.tetris_controlling = True
	
	stats.tetris_collide = False


def update_tetris(config, stats, blocks, current_tetris):
	if (stats.tetris_controlling and current_tetris.bottom_y == config.screen_row - 1) or stats.tetris_collide:
		stats.tetris_controlling = False
		check_completed_lines(config, blocks)


def check_completed_lines(config, blocks):
	row_index = 0
	while row_index < config.screen_row:
		column_index = 0
		checker = True
		while column_index < config.screen_column:
			if blocks[row_index][column_index].color == config.bg_color:
				checker = False
				break
			column_index += 1
		if checker:
			update_completed_line(blocks, row_index)
		else:
			row_index += 1


def update_completed_line(blocks, row_index):
	while row_index > 0:
		for column_index in range(len(blocks[row_index])):
			blocks[row_index][column_index].color = blocks[row_index - 1][column_index].color
		row_index -= 1


def draw_blocks(blocks):
	for row_index in range(len(blocks)):
		for column_index in range(len(blocks[0])):
			blocks[row_index][column_index].draw_block()


def draw_grid(config, screen):
	for x in range(0, config.play_screen_width, config.block_size):
		pygame.draw.line(screen, config.grid_color, (x, 0), (x, config.play_screen_height))
	for y in range(0, config.play_screen_height, config.block_size):
		pygame.draw.line(screen, config.grid_color, (0, y), (config.play_screen_width, y))


def update_screen(config, screen, stats, blocks, play_button, current_tetris):
	screen.fill(config.bg_color)
	
	if stats.game_active is False:
		draw_grid(config, screen)
		play_button.draw_button()
	else:
		draw_blocks(blocks)
		draw_grid(config, screen)
		# scoreboard.draw_scoreboard()
	
	if stats.tetris_controlling and not stats.tetris_collide:
		if stats.manual_timer_running is False:
			stats.manual_timer_running = True
			pygame.time.set_timer(pygame.USEREVENT + 1, config.tetris_manual_moving_speed)
			
			if current_tetris.moving_left:
				current_tetris.update_pos(blocks, (-1, 0))
			elif current_tetris.moving_right:
				current_tetris.update_pos(blocks, (1, 0))
			elif current_tetris.rotate_tetris:
				current_tetris.rotate(blocks)
		
		if stats.rotate_timer_running is False:
			stats.rotate_timer_running = True
			pygame.time.set_timer(pygame.USEREVENT + 2, config.tetris_rotate_speed)
		
		if stats.auto_timer_running is False:
			stats.auto_timer_running = True
			pygame.time.set_timer(pygame.USEREVENT + 3, config.tetris_auto_moving_speed)
			
			if current_tetris.moving_down:
				current_tetris.update_pos(blocks, (0, 1))
				current_tetris.moving_down = False
			
	pygame.display.flip()
