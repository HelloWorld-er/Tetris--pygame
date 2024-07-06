import pygame
import sys


class UISetting:
	"""
	Set the UI properties of a specific region.
	
	Methods:
		__init__: initializes the object and the UI properties.
	
	Attributes:
		screen_width: the width of the region the object is used for.
		screen_height: the height of the region the object is used for.
		bg_color: the background color of the UI object.
	
	"""
	def __init__(self, screen_width=1200, screen_height=800, screen_caption="", bg_color=(255, 255, 255)):
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.screen_caption = screen_caption
		self.bg_color = bg_color


class Grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height


def check_loop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# If the close button is pressed, quit the game
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			# Key down
			if event.key == pygame.K_q:
				# If key Q is pressed, quit the game
				sys.exit()


def main():
	pygame.init()
	
	main_window_ui = UISetting(screen_width=1200, screen_height=800, screen_caption="Tetris", bg_color=(60, 60, 60))
	
	screen = pygame.display.set_mode((main_window_ui.screen_width, main_window_ui.screen_height))
	pygame.display.set_caption(main_window_ui.screen_caption)
	
	while True:
		check_loop()
		
		screen.fill(main_window_ui.bg_color)
		pygame.display.flip()


if __name__ == '__main__':
	main()
