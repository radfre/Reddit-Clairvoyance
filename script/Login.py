import tkinter as tk
import praw

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reddit Login")
        self.client_id = ""
        self.client_secret = ""
        self.user_agent = ""
        self.reddit = None

        # Create input fields and labels
        tk.Label(self.root, text="Client ID").grid(row=0)
        self.client_id_entry = tk.Entry(self.root)
        self.client_id_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Client Secret").grid(row=1)
        self.client_secret_entry = tk.Entry(self.root, show="*")
        self.client_secret_entry.grid(row=1, column=1)

        tk.Label(self.root, text="User Agent").grid(row=2)
        self.user_agent_entry = tk.Entry(self.root)
        self.user_agent_entry.grid(row=2, column=1)

        # Create login button
        tk.Button(self.root, text="Login", command=self.login).grid(row=3, column=1)

    def show(self):
        self.root.mainloop()

    def login(self):
        self.client_id = self.client_id_entry.get()
        self.client_secret = self.client_secret_entry.get()
        self.user_agent = self.user_agent_entry.get()
        self.reddit = praw.Reddit(client_id=self.client_id,
                                  client_secret=self.client_secret,
                                  user_agent=self.user_agent)

        # Close the window
        self.root.destroy()
