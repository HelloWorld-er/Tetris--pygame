from pygame.sprite import Sprite, Group
from block import Block
import random


class Tetris(Sprite):
	def __init__(self, config, screen):
		super(Tetris, self).__init__()
		self.config = config
		self.screen = screen
		self.group = Group()
		self.color = random.choice(self.config.tetris_colors)[1]
		self.pattern = random.choice(self.config.tetris_patterns)
		
		self.create_fleet()
	
	def create_fleet(self):
		for block_pos in self.pattern:
			self.group.add(Block(self.config, self.screen, self.color, block_pos))
	