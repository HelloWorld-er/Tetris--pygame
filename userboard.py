import tkinter as tk


class UserBoard():
	def __init__(self, root, config, stats, scoreboard):
		self.config = config
		self.stats = stats
		self.scoreboard = scoreboard
		
		self.window = tk.Frame(root, borderwidth=1, relief="solid")
		
		self.username = ""
		
		self.username_entry_hint = tk.Label(self.window, text="Username: ")
		self.username_entry = tk.Entry(self.window)
		self.username_commit_button = tk.Button(self.window, text="Commit", command=self.retrieve_input)
		
		self.username_empty_hint = tk.Label(self.window, text="Username cannot be empty!", fg="red")
	
	def retrieve_input(self):
		input_value = self.username_entry.get()
		if input_value:
			self.username = input_value
			self.stats.login = True
			self.scoreboard.username = self.username
			self.scoreboard.initialize_records()
			
			if self.username_empty_hint.winfo_ismapped():
				self.username_empty_hint.pack_forget()
		else:
			self.username_empty_hint.pack()
		
	
	def place_user_board(self):
		self.window.place(relx=self.config.play_screen_width / self.config.screen_width,
		                  rely=self.config.scoreboard_height / self.config.screen_height,
		                  relwidth=self.config.userboard_width / self.config.screen_width,
		                  relheight=self.config.userboard_height / self.config.screen_height)
		self.username_entry_hint.pack(side='left')
		self.username_entry.pack(side='left')
		self.username_commit_button.pack(side='left')
