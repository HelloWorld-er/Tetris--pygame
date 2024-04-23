import os
import tkinter as tk

import tetris_game
from settings import Settings


def run_program():
	root = tk.Tk()
	root.title("Tetris")
	config = Settings()
	# root.geometry(f"{config.screen_width}x{config.screen_height}+{int((root.winfo_screenwidth()-config.screen_width)/2)}+{int((root.winfo_screenheight()-config.screen_height)/2)}")
	root.geometry(f"{config.screen_width}x{config.screen_height}")
	# game_window = tk.Frame(root, width=config.play_screen_width, height=config.play_screen_height)
	# game_window.grid(row=0, column=0)
	
	# os.environ["SDL_WINDOWID"] = str(game_window.winfo_id())
	
	# label = tk.Label(root, text="hello")
	# label.grid(row=0, column=1)
	
	root.mainloop()
	
	# tetris_game.run_game(config)


run_program()
