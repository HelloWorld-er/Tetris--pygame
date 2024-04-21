from pygame.sprite import Sprite, Group
import random


class Tetris(Sprite):
	def __init__(self, config, screen):
		super(Tetris, self).__init__()
		self.config = config
		self.screen = screen
		self.group = Group()
		self.color = random.choice(self.config.tetris_colors)[1]
		self.pattern = random.choice(self.config.tetris_patterns)
		self.origin = [random.randint(0, int(self.config.screen_column - max([_[0] for _ in self.pattern]))), 0]
	
	def update_pos(self, origin_pos):
		self.origin[0] += origin_pos[0]
		self.origin[1] += origin_pos[1]
		for block in self.group.sprites():
			block.update_pos(self.origin)
	
	def draw_tetris(self):
		for block in self.group.sprites():
			block.draw_block()
	