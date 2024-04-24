import tkinter as tk

import tetris_game


def prep_run_game(config, stats, scoreboard_window, x=0, y=0):
	if not stats.login:
		return
	tetris_game.run_game(config, stats, scoreboard_window, x, y)
	