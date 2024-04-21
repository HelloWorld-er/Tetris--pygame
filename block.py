import pygame
from pygame.sprite import Sprite


class Block(Sprite):
	"""For each block in a tetris"""
	def __init__(self, config, screen, color, block_pos):
		super(Block, self).__init__()
		self.config = config
		self.screen = screen
		self.color = color
		
		self.rect = pygame.Rect(block_pos[0], block_pos[1], self.config.block_size, self.config.block_size)
		self.rect.x = self.rect.width * block_pos[0]
		self.rect.y = self.rect.height * block_pos[1]
	
	def update_pos(self, origin_pos):
		self.rect.x += origin_pos[0] * self.rect.width
		self.rect.y += origin_pos[1] * self.rect.height
	
	def draw_block(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		