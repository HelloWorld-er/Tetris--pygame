import pygame
from pygame.rect import Rect
import pygame.font


class ScoreBoard():
	def __init__(self, config, stats, screen):
		self.config = config
		self.screen = screen
		
		self.bg_color = self.config.bg_color
		self.text_color = (0, 0, 0)
		
		self.highest_score = 0
		self.current_score = 0
		
		self.font = pygame.font.SysFont(None, 30)
		self.width = self.config.scoreboard_width
		self.height = 50
		
		self.highest_score_rect = Rect(5 + self.config.play_screen_width, 10, self.width, self.height)
		self.current_score_rect = Rect(5 + self.config.play_screen_width, 10 + self.height, self.width, self.height)
		
		self.highest_score_hint = "Highest Score: "
		self.current_score_hint = "Current Score: "
		
		self.prep_msg()
	
	def prep_msg(self):
		self.highest_score_msg_image = self.font.render(self.highest_score_hint + str(self.highest_score), True, self.text_color, self.bg_color)
		self.highest_score_msg_image_rect = self.highest_score_msg_image.get_rect()
		self.highest_score_msg_image_rect.x = self.highest_score_rect.x
		self.highest_score_msg_image_rect.centery = self.highest_score_rect.centery
		
		self.current_score_msg_image = self.font.render(self.current_score_hint + str(self.current_score), True, self.text_color, self.bg_color)
		self.current_score_msg_image_rect = self.current_score_msg_image.get_rect()
		self.current_score_msg_image_rect.x = self.current_score_rect.x
		self.current_score_msg_image_rect.centery = self.current_score_rect.centery
	
	def draw_scoreboard(self):
		self.screen.fill(self.bg_color, self.highest_score_rect)
		self.screen.blit(self.highest_score_msg_image, self.highest_score_msg_image_rect)
		
		self.screen.fill(self.bg_color, self.current_score_rect)
		self.screen.blit(self.current_score_msg_image, self.current_score_msg_image_rect)
		
	def update_score(self):
		if self.highest_score <= self.current_score:
			self.highest_score = self.current_score
			
