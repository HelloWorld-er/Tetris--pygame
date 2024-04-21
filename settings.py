class Settings():
	def __init__(self):
		self.screen_width = 600
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.grid_color = (0, 0, 0)
		
		self.block_size = 20
		self.screen_row = self.screen_height / self.block_size
		self.screen_column = self.screen_width / self.block_size
		
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
			((0, 0), (1, 0), (2, 0))
		]
