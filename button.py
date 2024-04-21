import pygame
from pygame.rect import Rect
import pygame.font


class Button():
	def __init__(self, config, screen, msg):
		self.config = config
		self.screen = screen
		
		self.width = 120
		self.height = 80
		self.button_color = (100, 20, 0)
		self.text_color = (210, 150, 10)
		
		self.rect = Rect(0, 0, self.width, self.height)
		
		self.font = pygame.font.SysFont(None, 40)
		
		self.prep_msg(msg)
	
	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
	
	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
