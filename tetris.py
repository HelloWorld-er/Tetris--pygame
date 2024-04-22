from pygame.sprite import Group
import random


class Origin():
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Tetris():
	def __init__(self, config, screen, stats):
		self.config = config
		self.screen = screen
		self.stats = stats
		
		self.group = Group()
		
		self.color = None
		self.pattern = None
		
		self.moving_left = False
		self.moving_right = False
		self.moving_down = False
		self.rotate_tetris = False
		
		self.left_x = 0
		self.right_x = 0
		self.top_y = 0
		self.bottom_y = 0
		
		self.origin = Origin(0, 0)
	
	def initialize_tetris(self, blocks):
		self.clean_up_group(True)
		
		self.color = random.choice(self.config.tetris_colors)
		self.pattern = [[__ for __ in _] for _ in random.choice(self.config.tetris_patterns)]
		
		self.set_up_boundaries()
		
		self.origin.x = random.randint(0, self.config.screen_column - self.right_x - 1)
		self.origin.y = 0
		
		self.add_blocks(blocks)
	
	def add_blocks(self, blocks):
		for block_rel_pos_column, block_rel_pos_row in self.pattern:
			expected_pos = (self.origin.x + block_rel_pos_column, self.origin.y + block_rel_pos_row)
			if any(_ < 0 for _ in expected_pos):
				continue
			try:
				blocks[expected_pos[1]][expected_pos[0]].add_to_group(self)
			except IndexError:
				pass
	
	def update_pos(self, blocks, origin_pos):
		if self.collision_detect(blocks, origin_pos):
			if origin_pos[1] == 1:
				self.stats.tetris_collide = True
			return
		
		self.origin.x += origin_pos[0]
		self.origin.y += origin_pos[1]
		
		self.clean_up_group(False)
		
		self.add_blocks(blocks)
	
	def collision_detect(self, blocks, origin_pos):
		if self.origin.x + self.left_x + origin_pos[0] < 0 or self.origin.x + self.right_x + origin_pos[0] >= self.config.screen_column:
			return True
		if self.origin.y + self.bottom_y + origin_pos[1] >= self.config.screen_row:
			return True
		
		for block_relative_pos in self.pattern:
			expected_pos = (self.origin.x + origin_pos[0] + block_relative_pos[0],
			                self.origin.y + origin_pos[1] + block_relative_pos[1])
			if expected_pos[0] < 0 or expected_pos[1] < 0:
				continue
			if expected_pos[0] >= self.config.screen_column or expected_pos[1] >= self.config.screen_row:
				continue
			
			if (not blocks[expected_pos[1]][expected_pos[0]].in_group(self)
					and blocks[expected_pos[1]][expected_pos[0]].color != self.config.bg_color):
				return True
		return False
	
	def rotate(self, blocks):
		old_patter = [[__ for __ in _] for _ in self.pattern]
		for index in range(len(old_patter)):
			self.pattern[index][0] = - old_patter[index][1]
			self.pattern[index][1] = old_patter[index][0]
		
		self.set_up_boundaries()
		
		if self.collision_detect(blocks, (0, 0)):
			self.pattern = [[__ for __ in _] for _ in old_patter]
			self.set_up_boundaries()
			return
		
		self.clean_up_group(False)
		
		self.add_blocks(blocks)
	
	def set_up_boundaries(self):
		self.left_x = min(_[0] for _ in self.pattern)
		self.right_x = max(_[0] for _ in self.pattern)
		self.top_y = min(_[1] for _ in self.pattern)
		self.bottom_y = max(_[1] for _ in self.pattern)
	
	def clean_up_group(self, save_color):
		for block in self.group.sprites():
			block.remove_from_group(save_color)
	
	def draw_tetris(self):
		for block in self.group.sprites():
			block.draw_block()
