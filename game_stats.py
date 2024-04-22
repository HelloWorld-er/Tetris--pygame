class GameStats():
	def __init__(self):
		self.game_active = False
		self.tetris_controlling = False
		
		self.auto_timer_running = False
		self.manual_timer_running = False
		self.rotate_timer_running = False
		
		self.tetris_collide = False
