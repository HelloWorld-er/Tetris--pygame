import pygame
from pygame.sprite import Sprite


class Block(Sprite):
	def __init__(self, config, screen, color, block_pos):
		super(Block, self).__init__()
		self.config = config
		self.screen = screen
		self.color = color
		self.block_pos_column = block_pos[0]
		self.block_pos_row = block_pos[1]
		
		self.rect = pygame.Rect(self.block_pos_column, self.block_pos_row, self.config.block_size, self.config.block_size)
		self.rect.x = self.rect.width * self.block_pos_column
		self.rect.y = self.rect.height * self.block_pos_row
		
		self.tetris = None
	
	def add_to_group(self, tetris):
		self.tetris = tetris
		self.tetris.group.add(self)
		self.color = self.tetris.color
	
	def remove_from_group(self, save_color):
		if not save_color:
			self.color = self.config.bg_color
		self.tetris.group.remove(self)
		self.tetris = None
	
	def in_group(self, tetris):
		return self.tetris == tetris
	
	def draw_block(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		