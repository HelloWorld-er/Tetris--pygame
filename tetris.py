from pygame.sprite import Group
import random


class Tetris():
	def __init__(self, config, screen):
		super(Tetris, self).__init__()
		self.config = config
		self.screen = screen
		
		self.group = None
		
		self.color = None
		self.pattern = None
		
		self.moving_left = False
		self.moving_right = False
		self.moving_down = False
		
		self.origin = []
	
		# self.origin = [random.randint(0, int(self.config.screen_column - max([_[0] for _ in self.pattern]))), 0]
	def initialize_tetris(self, blocks):
		self.group = Group()
		self.color = random.choice(self.config.tetris_colors)[1]
		self.pattern = random.choice(self.config.tetris_patterns)
		self.origin = [
			random.randint(0, int(self.config.screen_column - max([_[0] for _ in self.pattern])) - 1), 0]
		self.update_pos(blocks, (0, 0))
	
	def update_pos(self, blocks, origin_pos):
		self.origin[0] += origin_pos[0]
		self.origin[1] += origin_pos[1]
		
		for block in self.group.sprites():
			block.remove_from_group()
		
		for block_relative_pos in self.pattern:
			expected_pos = (self.origin[0] + block_relative_pos[0], self.origin[1] + block_relative_pos[1])
			if expected_pos[0] < 0 or expected_pos[1] < 0:
				continue
			try:
				blocks[expected_pos[1]][expected_pos[0]].add_to_group(self)
			except IndexError:
				pass
	
	def draw_tetris(self):
		for block in self.group.sprites():
			block.draw_block()
	