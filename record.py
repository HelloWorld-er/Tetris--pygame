import pygame


class Record():
	def __init__(self, config, screen, msg_hint, record):
		self.config = config
		self.screen = screen
		
		self.text_color = (0, 0, 0)
		
		self.font = pygame.font.SysFont(None, 30)
		
		self.record_hint = msg_hint
		self.record = record
		
		self.prep_record_hint()
	
	def prep_record_hint(self):
		self.msg_image = self.font.render(f"{self.record_hint}: {str(self.record)}", True, self.text_color, self.config.bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
	
	def draw_record(self):
		# self.screen.fill(self.config.bg_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
