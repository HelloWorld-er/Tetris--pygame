import tkinter as tk
from tkinter import font

import tetris_game
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from userboard import UserBoard


def run_program():
	root = tk.Tk()
	root.title("Tetris")
	
	config = Settings()
	stats = GameStats()
	
	root.geometry(
		f"{config.screen_width}x{config.screen_height}+{int((root.winfo_screenwidth() - config.screen_width) / 2)}+0")
	
	scoreboard_window = ScoreBoard(root, config, stats)
	scoreboard_window.place_scoreboard()
	
	user_board_window = UserBoard(root, config, stats, scoreboard_window)
	user_board_window.place_user_board()
	
	game_window = tk.Frame(root, width=config.play_screen_width, height=config.play_screen_height, borderwidth=1,
	                       relief="solid")
	game_window.place(relx=0, rely=0)
	
	game_window_button = tk.Button(game_window, text="Game Window", font=font.Font(size=40))
	game_window_button.place(relwidth=1, relheight=1, relx=0.5, rely=0.5, anchor='center')
	game_window_button.config(command=lambda: tetris_game.run_game(config, stats, scoreboard_window, int((root.winfo_screenwidth() - config.screen_width) / 2),0))
	
	root.mainloop()


# def login():


run_program()
