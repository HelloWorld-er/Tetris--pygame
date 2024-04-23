import json
import tkinter as tk
from tkinter import font


class ScoreBoard():
	def __init__(self, root, config, stats):
		self.config = config
		
		self.window = tk.Frame(root, borderwidth=1, relief="solid")
		
		self.username = None
		
		self.highest_score = 0
		self.user_highest_score = 0
		self.user_current_score = 0
		
		# self.initialize_records()
		
		self.font = font.Font(size=15)
		
		self.highest_score_label = tk.Label(self.window, text=f"Highest score(every users):\n{self.highest_score}",
		                                    font=self.font)
		self.user_highest_score_label = tk.Label(self.window,
		                                         text=f"Highest score(current user):\n{self.user_highest_score}",
		                                         font=self.font)
		self.user_current_score_label = tk.Label(self.window, text=f"Current score:\n{self.user_current_score}",
		                                         font=self.font)
		
		self.update_records()
	
	def place_scoreboard(self):
		self.window.place(relx=self.config.play_screen_width / self.config.screen_width, rely=0,
		                  relwidth=self.config.scoreboard_width / self.config.screen_width,
		                  relheight=self.config.scoreboard_height / self.config.screen_height)
		self.highest_score_label.pack(fill="x", side=tk.TOP)
		self.user_highest_score_label.pack(fill="x", side=tk.TOP)
		self.user_current_score_label.pack(fill="x", side=tk.TOP)
	
	def initialize_records(self):
		with open("users_data.json", "r+") as users_data_file:
			users_data = json.load(users_data_file)
			print(users_data)
			if users_data:
				self.highest_score = users_data['highest']['score']
				if self.username in users_data:
					self.user_highest_score = users_data[self.username]['score']
				else:
					users_data[self.username] = {"score": 0}
			else:
				users_data['highest'] = {"username": None, "score": 0}
				users_data[self.username] = {"score": 0}
			
			users_data_file.seek(0, 0)
			json.dump(users_data, users_data_file, indent=4)
		
		self.update_records()
	
	def update_records(self):
		if self.user_highest_score < self.user_current_score:
			self.user_highest_score = self.user_current_score
		if self.highest_score < self.user_highest_score:
			self.highest_score = self.user_highest_score
		self.highest_score_label.config(text=f"Highest score(every users):\n{self.highest_score}")
		self.user_highest_score_label.config(text=f"Highest score(current user):\n{self.user_highest_score}")
		self.user_current_score_label.config(text=f"Current score:\n{self.user_current_score}")
	
	def store_data(self):
		with open("users_data.json", "r+") as users_data_file:
			users_data = json.load(users_data_file)
			users_data[self.username]['score'] = self.user_highest_score
			if users_data["highest"]["score"] <= self.user_highest_score:
				users_data["highest"]["username"] = self.username
				users_data["highest"]["score"] = self.user_highest_score
			
			users_data_file.seek(0, 0)
			json.dump(users_data, users_data_file, indent=4)
