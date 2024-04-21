import pygame
from pygame.sprite import Sprite


class Block(Sprite):
	def __init__(self, config, screen, color, block_pos):
		super(Block, self).__init__()
		self.config = config
		self.screen = screen
		self.color = color
		self.block_pos = block_pos
		
		self.rect = pygame.Rect(block_pos[0], block_pos[1], self.config.block_size, self.config.block_size)
		self.rect.x = self.rect.width * block_pos[0]
		self.rect.y = self.rect.height * block_pos[1]
		
		self.tetris = None
	
	def add_to_group(self, tetris):
		self.tetris = tetris
		self.tetris.group.add(self)
		self.color = self.tetris.color
	
	def remove_from_group(self):
		self.color = self.config.bg_color
		self.tetris.group.remove(self)
		self.tetris = None
	
	def draw_block(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		