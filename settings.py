class Settings():
	def __init__(self):
		self.screen_width = 1000
		self.screen_height = 800
		
		self.play_screen_width = 600
		self.play_screen_height = 800
		
		self.scoreboard_width = self.screen_width - self.play_screen_width
		self.scoreboard_height = 800
		
		# self.userboard_width = self.screen_width - self.play_screen_width
		# self.userboard_height = int(self.screen_height/4)
		
		self.bg_color = (230, 230, 230)
		self.grid_color = (0, 0, 0)
		
		self.block_size = 20
		self.screen_row = int(self.play_screen_height / self.block_size)
		self.screen_column = int(self.play_screen_width / self.block_size)
		
		self.tetris_colors = [
			(0, 255, 255),  # Cyan
			(255, 255, 0),  # Yellow
			(128, 0, 128),  # Purple
			(0, 255, 0),  # Green
			(255, 0, 0),  # Red
			(0, 0, 255),  # Blue
			(255, 127, 0),  # Orange
			(127, 127, 127)  # Grey
		]
		self.tetris_patterns = [
			((0, 0), (1, 0), (2, 0)),
			((0, 0), (1, 0), (0, -1), (1, -1)),
			((0, 0), (0, -1), (1, -1)),
			((0, 0), (0, -1), (0, -2), (0, -3)),
			((0, 0), (1, 0), (2, 0), (1, -1)),
			((0, 0), (1, 0), (0, -1), (0, -2), (0, -3)),
			((0, 0), (2, 0), (0, -1), (1, -1), (2, -1), (3, -1)),
			((0, 0), (1, 0), (1, -1), (2, -1)),
			((0, 0), (1, 0), (0, -1), (1, -1), (0, -2), (1, -2))
		]
		
		self.tetris_auto_moving_speed = 100
		self.tetris_manual_moving_speed = 70
		self.tetris_rotate_speed = 100
