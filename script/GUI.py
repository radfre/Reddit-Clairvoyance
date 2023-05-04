import tkinter as tk


class GUI:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.title('Reddit Top Posts')
        self.window.geometry('800x500')
        self.window.configure(bg='gray')

        # Create label to display results
        self.Title_label = tk.Label(self.window, text='', justify='left')
        self.Top_label = tk.Label(self.window, text='', justify='left')
        self.Users_label = tk.Label(self.window, text='', justify='left')

        self.frame1 = tk.Frame(self.window, tk.GROOVE, borderwidth=10)

        self.Title_label.pack(self.frame1)
        self.Top_label.pack(self.frame1)
        self.Users_label(self.frame1)

        self.frame1.pack(tk.LEFT)

        self.Users_label.pack()


    def loading(self):
        print('loading')

    def display_top_posts(self, top_posts_text):
        self.Top_label.config(text=top_posts_text)
        self.window.mainloop()
