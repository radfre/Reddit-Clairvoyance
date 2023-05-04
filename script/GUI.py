import tkinter as tk


class GUI:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.title('Reddit Top Posts')
        self.window.geometry('400x800')

        # Create label to display results
        self.result_label = tk.Label(self.window, text='', justify='left')
        self.result_label.pack()

    def loading(self):
        print('loading')

    def display_top_posts(self, top_posts_text):
        self.result_label.config(text=top_posts_text, justify='left')
        self.window.mainloop()
