from record import Record

class ScoreBoard():
	def __init__(self, config, screen):
		self.config = config
		self.screen = screen
		
		self.highest_score = Record(self.config, self.screen, "Highest score(every users)", 0)
		self.user_highest_score = Record(self.config, self.screen, "Highest score(current user)", 0)
		self.user_current_score = Record(self.config, self.screen, "Current score", 0)
		
		self.highest_score.msg_image_rect.x = self.config.play_screen_width + 30
		self.highest_score.msg_image_rect.y = 10
		self.user_highest_score.msg_image_rect.x = self.config.play_screen_width + 30
		self.user_highest_score.msg_image_rect.y = self.highest_score.msg_image_rect.bottom + 30
		self.user_current_score.msg_image_rect.x = self.config.play_screen_width + 30
		self.user_current_score.msg_image_rect.y = self.user_highest_score.msg_image_rect.bottom + 30
	
	def draw_scoreboard(self):
		self.highest_score.draw_record()
		self.user_highest_score.draw_record()
		self.user_current_score.draw_record()
		