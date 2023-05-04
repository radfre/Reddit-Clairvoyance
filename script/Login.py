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
        tk.Label(self.root, text="Client ID").grid(row=0, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self.root)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Client Secret").grid(row=1, padx=10, pady=10)
        self.client_secret_entry = tk.Entry(self.root, show="0")
        self.client_secret_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="User Agent").grid(row=2, padx=10, pady=10)
        self.user_agent_entry = tk.Entry(self.root)
        self.user_agent_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create login button
        tk.Button(self.root, text="Login", command=self.login).grid(row=3, column=1, padx=10, pady=10)

    def show(self):
        self.root.mainloop()

    def login(self):
        # Close the window
        self.client_id = self.client_id_entry.get()
        self.client_secret = self.client_secret_entry.get()
        self.user_agent = self.user_agent_entry.get()
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret,
                                  user_agent=self.user_agent)
        self.root.destroy()

    def getClientID(self):
        return self.client_id_entry.get()

    def getClientSecret(self):
        return self.client_secret_entry.get()

    def getUserAgent(self):
        return self.user_agent_entry.get()
